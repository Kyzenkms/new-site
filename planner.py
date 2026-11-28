"""Planner: deterministic day-by-day revision plan from extracted topics.

No model calls here - the plan is arithmetic, so it can be checked.
Topics come from the notes' own headings (markdown #, numbered units,
or ALL-CAPS lines), so the plan is built from the student's material,
never invented.
"""
from __future__ import annotations

import re
from datetime import date, timedelta

from safety import find_dates, parse_date

_HEADING = re.compile(r"^#{1,3}\s+(.+)$")
_NUMBERED = re.compile(r"^(?:unit|chapter|topic)\s*\d+[:.\s-]+(.+)$", re.IGNORECASE)
_CONTEXT_WORDS = re.compile(
    r"(?i)exam|test|paper|deadline|viva|submission|due|closes|closing|submit|hand in")


_NOISE = ("study notes", "topic list", "likely exam questions", "topics covered",
          "marking tip", "contents", "cae-1", "cae-2")


def extract_topics(text: str, fallback_name: str) -> list[str]:
    topics: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        m = _HEADING.match(line) or _NUMBERED.match(line)
        if m:
            topic = m.group(1).strip().strip("#").strip()
            low = topic.lower()
            if any(n in low for n in _NOISE):
                continue
            if 3 <= len(topic) <= 90 and low not in (t.lower() for t in topics):
                topics.append(topic)
    if not topics:
        topics = [fallback_name]
    return topics


def subject_of(filename: str) -> str:
    name = re.sub(r"[-_]+", " ", filename.rsplit(".", 1)[0]).strip()
    name = re.sub(r"(?i)\bcae\s*\d\b", "", name).strip()
    name = re.sub(r"(?i)\bnotes?\b", "", name).strip()
    return name.upper() if len(name) <= 5 else name.title()


def note_dates(text: str) -> list[str]:
    """Dates that appear near exam/deadline words in a note."""
    out = []
    for d in find_dates(text):
        for m in re.finditer(re.escape(d), text):
            window = text[max(0, m.start() - 45): m.end() + 45]
            if _CONTEXT_WORDS.search(window) and d not in out:
                out.append(d)
    return out


def _balanced(items: list[str], n: int) -> list[list[str]]:
    """Split items into n contiguous groups, sizes differing by at most 1."""
    if n <= 0:
        return []
    base, extra = divmod(len(items), n)
    out, i = [], 0
    for k in range(n):
        size = base + (1 if k < extra else 0)
        out.append(items[i:i + size])
        i += size
    return out


def build_plan(subjects: dict[str, list[str]], start: date,
               exam_dates: dict[str, date], default_exam: date) -> list[dict]:
    """Day-by-day plan honouring each subject's own exam date.

    A subject's topics land only on days before its exam, spread evenly;
    its last day before the exam is a revision pass. Subjects interleave
    across each day instead of being taken one at a time.
    """
    exams = {s: exam_dates.get(s, default_exam) for s in subjects}
    if not exams:
        return []
    last = max(exams.values())
    n_days = (last - start).days
    if n_days <= 0:
        return [{"date": default_exam.isoformat(), "kind": "exam-day",
                 "items": ["Exam day - no new material."]}]
    days = [start + timedelta(days=i) for i in range(n_days)]
    per_day: dict[date, list[str]] = {d: [] for d in days}
    for subj, topics in subjects.items():
        avail = [d for d in days if d < exams[subj]]
        if not avail or not topics:
            continue
        study_days = avail[:-1] if len(avail) > 1 else avail
        units = [f"{subj}: {t}" for t in topics]
        for d, chunk in zip(study_days, _balanced(units, len(study_days))):
            per_day[d].extend(chunk)
        if len(avail) > 1:
            per_day[avail[-1]].append(
                f"REVISION - {subj}: full pass over the plan, redo weak spots")
    plan = []
    for d in days:
        items = per_day[d]
        kind = ("revision" if items and all(i.startswith("REVISION") for i in items)
                else "study")
        plan.append({"date": d.isoformat(), "kind": kind,
                     "items": items or ["Open day - catch up on the weakest subject."]})
    return plan


def render_plan(plan: list[dict], exam_dates: dict[str, date], exam_source: str) -> str:
    lines = ["# Revision plan", "", "Exams:"]
    for subj in sorted(exam_dates):
        lines.append(f"- {subj}: {exam_dates[subj].isoformat()} ({exam_source})")
    lines.append("")
    for day in plan:
        lines.append(f"## {day['date']} ({day['kind']})")
        lines += [f"- {item}" for item in day["items"]]
        lines.append("")
    return "\n".join(lines)
