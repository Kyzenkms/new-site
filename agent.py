"""StudyPilot - a revision agent you can walk away from.

Drop study notes in a folder, give an exam date, and it runs unattended:
ingests the notes (treating every word in them as data, never as
instructions), builds a day-by-day revision plan, and writes an audit
trace of everything it saw and decided. When material is missing,
broken or contradictory, it stops and asks instead of inventing.

Safety, by construction:
- reads only the inbox folder, writes only the output folder
- never deletes anything; poisoned lines are removed, files are kept
- a STOP file in the inbox or output folder halts the run at the next step
- step budget caps how much work one run can do
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

import packs
import planner
import safety
from tools import ModelError, NoteError, Toolbox
from trace import Trace

MAX_STEPS_DEFAULT = 200


def load_dotenv(path: Path = Path(".env")) -> None:
    """Tiny .env reader - keeps dependencies at PyMuPDF only."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def stopped(stop_paths: list[Path]) -> bool:
    return any(p.exists() for p in stop_paths)


def main() -> int:
    ap = argparse.ArgumentParser(description="StudyPilot revision agent")
    ap.add_argument("--inbox", default="inbox", help="folder of notes to read")
    ap.add_argument("--output", default="output", help="folder for plan + trace")
    ap.add_argument("--exam-date", default=None,
                    help="exam date YYYY-MM-DD (yours outranks any date in the notes)")
    ap.add_argument("--exam-dates", default=None,
                    help="per-subject exam dates, e.g. 'IKS=2026-12-07,LAS=2026-12-09'")
    ap.add_argument("--start-date", default=None, help="plan start YYYY-MM-DD (default: today)")
    ap.add_argument("--max-steps", type=int, default=MAX_STEPS_DEFAULT)
    ap.add_argument("--mark-done", default=None, metavar="YYYY-MM-DD",
                    help="mark that plan day as completed, then exit")
    args = ap.parse_args()

    load_dotenv()
    inbox, output = Path(args.inbox), Path(args.output)
    box = Toolbox(inbox, output)
    trace = Trace(output / "trace.jsonl",
                  secrets=[os.environ.get("GEMINI_API_KEY", "")])
    stop_paths = [inbox / "STOP", output / "STOP"]
    steps = 0

    def step(event: str, **fields) -> bool:
        """Log one step; return False when the run must halt."""
        nonlocal steps
        if stopped(stop_paths):
            trace.log("killed", reason="STOP file present")
            print("STOP file found - halting cleanly.")
            return False
        steps += 1
        if steps > args.max_steps:
            trace.log("budget_exceeded", max_steps=args.max_steps)
            print("Step budget reached - halting.")
            return False
        trace.log(event, **fields)
        return True

    trace.log("run_start", inbox=str(inbox), output=str(output))
    print(f"StudyPilot run {trace.run_id}: reading {inbox} ...")

    progress_path = box.output / "progress.json"
    progress = {"plan": [], "done_topics": [], "done_days": []}
    if progress_path.exists():
        try:
            progress.update(json.loads(progress_path.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            trace.log("progress_unreadable", reason="progress.json is not valid JSON")

    if args.mark_done:
        day = next((d for d in progress["plan"] if d["date"] == args.mark_done), None)
        if day is None:
            print(f"No plan day {args.mark_done} in progress.json - nothing marked.")
            return 2
        for item in day["items"]:
            if item not in progress["done_topics"]:
                progress["done_topics"].append(item)
        if args.mark_done not in progress["done_days"]:
            progress["done_days"].append(args.mark_done)
        progress_path.write_text(json.dumps(progress, indent=1), encoding="utf-8")
        trace.log("day_marked_done", date=args.mark_done)
        print(f"Marked {args.mark_done} done ({len(day['items'])} item(s)). "
              "The next run reshuffles what remains.")
        return 0

    questions: list[str] = []
    subjects: dict[str, list[str]] = {}
    notes_by_subject: dict[str, str] = {}
    subject_note_dates: dict[str, list[str]] = {}
    report_lines: list[str] = ["# Ingest report", ""]

    files = box.list_inbox()
    if not step("inbox_listed", files=[f.name for f in files]):
        return 3
    if not files:
        questions.append("The inbox is empty - no notes to plan from. Add notes and re-run.")

    for path in files:
        if path.name == "STOP":
            continue
        if not step("read_note", file=path.name):
            return 3
        try:
            text, meta = box.read_note(path)
        except NoteError as e:
            trace.log("note_quarantined", file=path.name, reason=str(e))
            report_lines.append(f"- QUARANTINED `{path.name}`: {e}")
            print(f"  quarantined {path.name}: {e}")
            continue
        clean, srep = safety.sanitise(text)
        if srep["lines_removed"] or srep["zero_width_removed"]:
            trace.log("note_sanitised", file=path.name, **{
                "zero_width_removed": srep["zero_width_removed"],
                "lines_removed": len(srep["lines_removed"]),
            })
            report_lines.append(
                f"- SANITISED `{path.name}`: removed {len(srep['lines_removed'])} "
                f"instruction-like line(s), {srep['zero_width_removed']} invisible char(s). "
                "Content treated as data, never obeyed.")
            print(f"  sanitised {path.name}: {len(srep['lines_removed'])} planted line(s) removed")
        if meta.get("json_error"):
            trace.log("note_broken_data", file=path.name, detail=meta["json_error"])
            report_lines.append(f"- BROKEN DATA `{path.name}`: JSON error ({meta['json_error']}). "
                                "Recovered what parsed; flagged, not silently dropped.")
        for prob in box.last_problems:
            if prob == meta.get("json_error"):
                continue
            trace.log("note_data_problem", file=path.name, problem=prob)
            report_lines.append(f"- DATA PROBLEM `{path.name}`: {prob}")
        if not srep["salvageable"]:
            trace.log("note_quarantined", file=path.name,
                      reason="nothing salvageable after sanitising")
            report_lines.append(f"- QUARANTINED `{path.name}`: nothing but instruction-like "
                                "content - no study material to use.")
            continue
        subj = planner.subject_of(path.name)
        topics = planner.extract_topics(clean, subj)
        subjects.setdefault(subj, []).extend(
            t for t in topics if t not in subjects.get(subj, []))
        notes_by_subject[subj] = (notes_by_subject.get(subj, "") + "\n\n" + clean).strip()
        subject_note_dates.setdefault(subj, []).extend(
            d for d in planner.note_dates(clean)
            if d not in subject_note_dates.get(subj, []))
        report_lines.append(f"- OK `{path.name}` -> {subj}: {len(topics)} topic(s)"
                            + (f", {meta['pages']} page(s)" if meta.get("pages") else "")
                            + (f", encoding {meta['encoding']}" if meta.get("encoding") else ""))

    # ---- exam dates: the user's word outranks the notes ---------------
    exam = None
    exam_source = None
    if args.exam_date:
        exam = safety.parse_date(args.exam_date)
        if exam is None:
            questions.append(f"Your exam date '{args.exam_date}' is not a real calendar date.")
        else:
            exam_source = "given by you"
    exam_dates: dict[str, date] = {}
    if args.exam_dates:
        for pair in args.exam_dates.split(","):
            name, _, when = pair.partition("=")
            parsed = safety.parse_date(when.strip())
            if parsed is None:
                questions.append(f"Your exam date for {name.strip()} "
                                 f"('{when.strip()}') is not a real calendar date.")
            else:
                exam_dates[name.strip().upper()] = parsed
        if exam_dates and exam is None:
            exam, exam_source = max(exam_dates.values()), "given by you"

    default_year = (exam or date.today()).year
    all_note_dates: set[date] = set()
    broken_dates: list[str] = []
    conflicts: list[str] = []
    for subj, raws in subject_note_dates.items():
        parsed = set()
        for raw in raws:
            p = safety.parse_date(raw, default_year)
            if p is None:
                if raw not in broken_dates:
                    broken_dates.append(raw)
            else:
                parsed.add(p)
        all_note_dates |= parsed
        if len(parsed) > 1:
            report_lines.append(
                f"- DATES IN NOTES {subj}: "
                + ", ".join(d.isoformat() for d in sorted(parsed))
                + " - more than one date in the material; planned on yours.")
        subj_exam = exam_dates.get(subj.upper(), exam)
        if subj_exam is not None and parsed and subj_exam not in parsed:
            conflicts.append(
                f"{subj}: your date {subj_exam.isoformat()} vs note date(s) "
                + ", ".join(d.isoformat() for d in sorted(parsed)))
    if broken_dates:
        trace.log("broken_dates_flagged", dates=broken_dates)
        report_lines.append(f"- BROKEN DATA: impossible date(s) in notes: {', '.join(broken_dates)} "
                            "- flagged, not planned around.")
    if conflicts:
        trace.log("date_conflict", detail=conflicts)
        for c in conflicts:
            report_lines.append(f"- DATE CONFLICT: {c}. Planned on YOUR date; "
                                "the note dates are recorded here, not silently used.")
        print("  date conflict flagged: your date wins, notes recorded")
    if exam is None:
        if len(all_note_dates) == 1:
            exam, exam_source = next(iter(all_note_dates)), "found in your notes"
        elif len(all_note_dates) > 1:
            questions.append(
                "Your notes give more than one exam date ("
                + ", ".join(d.isoformat() for d in sorted(all_note_dates))
                + "). Which one is right?")
        else:
            questions.append("No exam date given and none found in the notes. "
                             "Re-run with --exam-date YYYY-MM-DD.")
    resolved = {s: exam_dates.get(s.upper(), exam) for s in subjects}

    start = safety.parse_date(args.start_date) if args.start_date else date.today()
    if not step("plan_built", exam=str(exam), subjects=list(subjects)):
        return 3

    box.write_output("ingest-report.md", "\n".join(report_lines) + "\n")
    if questions:
        box.write_output("QUESTIONS.md",
                         "# StudyPilot needs your word\n\n"
                         + "\n".join(f"- {q}" for q in questions) + "\n")
        trace.log("stop_and_ask", questions=questions)
        print("Stopped to ask - see output/QUESTIONS.md")
        return 2

    done = set(progress["done_topics"])
    if done:
        subjects = {s: [t for t in ts if f"{s}: {t}" not in done]
                    for s, ts in subjects.items()}
        subjects = {s: ts for s, ts in subjects.items() if ts}
        trace.log("reshuffle", done_topics=len(done))
        print(f"  reshuffled: {len(done)} finished item(s) left out of the new plan")

    plan = planner.build_plan(subjects, start, resolved, exam)
    box.write_output("plan.md", planner.render_plan(plan, resolved, exam_source))
    progress["plan"] = plan
    progress_path.write_text(json.dumps(progress, indent=1), encoding="utf-8")

    pack_note = ""
    if plan and plan[0]["kind"] == "study":
        if os.environ.get("GEMINI_API_KEY") or os.environ.get("MODEL_API_KEY"):
            if not step("pack_generate", date=plan[0]["date"]):
                return 3
            pack_md, stats = packs.build_pack(box, trace, plan[0], notes_by_subject)
            box.write_output(f"packs/{plan[0]['date']}.md", pack_md)
            pack_note = (f" Pack for {plan[0]['date']}: {stats['subjects_ok']} subject(s) "
                         f"generated, {stats['subjects_failed']} failed/skipped.")
            trace.log("pack_done", **stats)
        else:
            trace.log("pack_skipped", reason="no model API key configured")
            pack_note = " Pack skipped: no model API key configured."
    trace.log("run_done", days=len(plan), questions=0)
    span = ""
    if resolved:
        span = (f" Exams {min(resolved.values()).isoformat()} to "
                f"{max(resolved.values()).isoformat()}.")
    print(f"Done: {len(plan)} day(s), {len(subjects)} subject(s).{span} "
          f"See output/plan.md.{pack_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
