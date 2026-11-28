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
import os
import sys
from datetime import date
from pathlib import Path

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
    ap.add_argument("--start-date", default=None, help="plan start YYYY-MM-DD (default: today)")
    ap.add_argument("--max-steps", type=int, default=MAX_STEPS_DEFAULT)
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

    questions: list[str] = []
    subjects: dict[str, list[str]] = {}
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
        report_lines.append(f"- OK `{path.name}` -> {subj}: {len(topics)} topic(s)"
                            + (f", {meta['pages']} page(s)" if meta.get("pages") else "")
                            + (f", encoding {meta['encoding']}" if meta.get("encoding") else ""))

    # ---- exam date: the user's word outranks the notes ----------------
    exam = None
    exam_source = None
    if args.exam_date:
        exam = safety.parse_date(args.exam_date)
        if exam is None:
            questions.append(f"Your exam date '{args.exam_date}' is not a real calendar date.")
        else:
            exam_source = "given by you"
    note_date_strs: list[str] = []
    for path in files:
        try:
            raw_text, _ = box.read_note(path)
        except NoteError:
            continue
        note_date_strs += planner.note_dates(raw_text)
    parsed_note_dates = {d: safety.parse_date(d) for d in set(note_date_strs)}
    broken_dates = [d for d, p in parsed_note_dates.items() if p is None]
    valid_note_dates = sorted({p for p in parsed_note_dates.values() if p is not None})
    if broken_dates:
        trace.log("broken_dates_flagged", dates=broken_dates)
        report_lines.append(f"- BROKEN DATA: impossible date(s) in notes: {', '.join(broken_dates)} "
                            "- flagged, not planned around.")
    if exam is not None and valid_note_dates and exam not in valid_note_dates:
        trace.log("date_conflict", user_date=exam.isoformat(),
                  note_dates=[d.isoformat() for d in valid_note_dates])
        report_lines.append(
            f"- DATE CONFLICT: your date {exam.isoformat()} vs note date(s) "
            f"{', '.join(d.isoformat() for d in valid_note_dates)}. "
            "Planned on YOUR date; the note dates are recorded here, not silently used.")
        print("  date conflict flagged: your date wins, notes recorded")
    if exam is None:
        if len(valid_note_dates) == 1:
            exam, exam_source = valid_note_dates[0], "found in your notes"
        elif len(valid_note_dates) > 1:
            questions.append(
                "Your notes give more than one exam date ("
                + ", ".join(d.isoformat() for d in valid_note_dates)
                + "). Which one is right?")
        else:
            questions.append("No exam date given and none found in the notes. "
                             "Re-run with --exam-date YYYY-MM-DD.")

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

    plan = planner.build_plan(subjects, start, exam)
    box.write_output("plan.md", planner.render_plan(plan, exam, exam_source))
    trace.log("run_done", days=len(plan), questions=0)
    print(f"Done: plan for exam {exam.isoformat()} ({exam_source}), "
          f"{len(plan)} day(s), {len(subjects)} subject(s). See output/plan.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
