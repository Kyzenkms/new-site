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
_CONTEXT_WORDS = re.compile(r"(?i)exam|test|paper|deadline|viva|submission")


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


def build_plan(subjects: dict[str, list[str]], start: date, exam: date) -> list[dict]:
    """Spread topics over the days before the exam; exam eve = light revision."""
    days = (exam - start).days
    if days <= 0:
        return [{"date": exam.isoformat(), "kind": "exam-day",
                 "items": ["Exam day - no new material."]}]
    units = [(subj, topic) for subj, topics in subjects.items() for topic in topics]
    plan: list[dict] = []
    if not units:
        return plan
    study_days = max(days - 1, 1)  # last day before the exam is revision-only
    per_day = max(1, -(-len(units) // study_days))
    idx = 0
    for offset in range(days):
        day = start + timedelta(days=offset)
        if offset == days - 1:
            plan.append({"date": day.isoformat(), "kind": "revision",
                         "items": ["Full revision: skim every topic, redo weak quiz questions."]})
        else:
            todays = units[idx: idx + per_day]
            idx += len(todays)
            plan.append({"date": day.isoformat(), "kind": "study",
                         "items": [f"{s}: {t}" for s, t in todays]})
    return plan


def render_plan(plan: list[dict], exam: date, exam_source: str) -> str:
    lines = [f"# Revision plan - exam {exam.isoformat()} ({exam_source})", ""]
    for day in plan:
        lines.append(f"## {day['date']} ({day['kind']})")
        lines += [f"- {item}" for item in day["items"]]
        lines.append("")
    return "\n".join(lines)
