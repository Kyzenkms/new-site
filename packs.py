"""Pack generator: one day's revision pack - flashcards + quiz.

Grounding rule: the model only ever sees the student's own sanitised
notes for that subject, and the prompt forbids adding facts that are
not in them. If a subject's generation fails, the pack says so and
lists the topics - the run never crashes and never invents content
to fill the gap.
"""
from __future__ import annotations

from tools import ModelError, Toolbox
from trace import Trace

PROMPT = """You are StudyPilot, making today's revision pack for one subject.

Use ONLY the notes between the markers. Do not add facts, examples or
numbers that are not in the notes. If the notes are thin on a topic,
make fewer cards rather than inventing material.

Today's topics for {subject}: {topics}

=== NOTES START ===
{notes}
=== NOTES END ===

Write markdown with exactly these two sections:

## Flashcards
8 to 12 cards, each formatted as:
**Q:** ...
**A:** ...

## Quiz
5 multiple-choice questions on today's topics. Each question has four
options labelled A-D, and the correct letter is given immediately after
the question in the form [answer: B]. Keep questions factual and drawn
from the notes."""


def excerpt_for(notes: str, topics: list[str], cap: int = 30000) -> str:
    """The note sections that match today's topics, plus the intro.

    Beats head-truncation: on a long note, the sections for today's
    topics are what the pack must be grounded in, wherever they sit.
    """
    intro: list[str] = []
    sections: list[list[str]] = []
    current = None
    for line in notes.splitlines():
        if line.lstrip().startswith("#"):
            current = [line]
            sections.append(current)
        elif current is None:
            intro.append(line)
        else:
            current.append(line)
    wanted = [t.lower() for t in topics]
    picked = list(intro)
    for sec in sections:
        head = sec[0].lstrip("# ").strip().lower()
        if any(t in head or head in t for t in wanted):
            picked += sec
    text = "\n".join(picked).strip()
    return (text or notes)[:cap]


def build_pack(box: Toolbox, trace: Trace, day: dict,
               notes_by_subject: dict[str, str]) -> tuple[str, dict]:
    """Generate the pack for one plan day. Returns (markdown, stats)."""
    by_subject: dict[str, list[str]] = {}
    for item in day["items"]:
        if ": " in item:
            subj, topic = item.split(": ", 1)
            by_subject.setdefault(subj, []).append(topic)
    lines = [f"# Revision pack - {day['date']}", ""]
    stats = {"subjects_ok": 0, "subjects_failed": 0}
    for subj, topics in by_subject.items():
        notes = notes_by_subject.get(subj, "")
        lines.append(f"# {subj}")
        if not notes:
            lines += ["_No notes found for this subject - skipped, not invented._", ""]
            stats["subjects_failed"] += 1
            trace.log("pack_subject_skipped", subject=subj, reason="no notes")
            continue
        prompt = PROMPT.format(subject=subj, topics=", ".join(topics),
                               notes=excerpt_for(notes, topics))
        try:
            out = box.call_model(prompt, max_tokens=8192)
            if "## Quiz" not in out:
                trace.log("pack_incomplete", subject=subj,
                          reason="model output ended before the quiz section")
        except ModelError as e:
            lines += [f"_Generation failed for {subj} ({e}). Topics to revise "
                      f"from your notes directly: {', '.join(topics)}._", ""]
            stats["subjects_failed"] += 1
            trace.log("pack_subject_failed", subject=subj, reason=str(e))
            continue
        lines += [out.strip(), ""]
        stats["subjects_ok"] += 1
        trace.log("pack_subject_done", subject=subj, topics=len(topics))
    return "\n".join(lines), stats
