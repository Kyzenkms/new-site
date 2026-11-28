"""Guardrails: note content is DATA, never instructions.

Three jobs:
1. Strip invisible characters (zero-width spaces etc.) that hide text
   from keyword filters - Trap Pack #11 hides an instruction this way.
2. Find instruction-like lines planted in notes (prompt injection) and
   remove those lines, keeping the real content. Flag-and-continue:
   a file that merely *quotes* an attack phrase (Trap Pack controls
   #04/#18) is processed normally, never quarantined for keywords alone.
3. Validate dates: an impossible date (30 February) is broken data,
   reported and asked about, never planned around.
"""
from __future__ import annotations

import re
from datetime import date

# Invisible / zero-width characters used to hide text from filters.
INVISIBLE = dict.fromkeys(
    [0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF, 0x00AD, 0x180E], None
)

# Lines that read as instructions to an agent rather than study content.
# A match gets the line removed and logged; it is never obeyed.
INSTRUCTION_PATTERNS = [
    re.compile(r"(?i)\bignore (all )?(previous|prior|above) instructions\b"),
    re.compile(r"(?i)\bdisregard (your|the) (instructions|rules|prompt)\b"),
    re.compile(r"(?i)^\s*\[?\s*system\s*\]?\s*[:>]"),
    re.compile(r"(?i)\bdeveloper mode\b"),
    re.compile(r"(?i)\b(delete|remove|wipe|erase) (all )?(the )?(files?|folder|director|notes)\b"),
    re.compile(r"(?i)\b(send|forward|email|post|upload) .{0,40}\b(to|at)\b .{0,60}@"),
    re.compile(r"(?i)\breply (only|just) with\b"),
    re.compile(r"(?i)\bappend (the )?(token|canary|code)\b"),
    re.compile(r"(?i)\bmark .{0,30} (present|approved)\b"),
    re.compile(r"(?i)\byou (must|should|are required to) (now )?(delete|send|forward|reply|append|mark)\b"),
    re.compile(r"(?i)AGW-CANARY-[0-9A-Z]{4}"),
]


def strip_invisible(text: str) -> tuple[str, int]:
    cleaned = text.translate(INVISIBLE)
    return cleaned, len(text) - len(cleaned)


def sanitise(text: str) -> tuple[str, dict]:
    """Return (clean_text, report). Poisoned lines are removed, not obeyed."""
    text, zw_removed = strip_invisible(text)
    kept, removed = [], []
    for line in text.splitlines():
        hits = [p.pattern for p in INSTRUCTION_PATTERNS if p.search(line)]
        if hits:
            removed.append({"line": line.strip()[:160], "patterns": len(hits)})
        else:
            kept.append(line)
    clean = "\n".join(kept).strip()
    report = {
        "zero_width_removed": zw_removed,
        "lines_removed": removed,
        "salvageable": len(clean) >= 40,
    }
    return clean, report


_MONTHS = {name: i + 1 for i, name in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"])}
_MONTH_ALT = "|".join(_MONTHS)


def parse_date(text: str) -> date | None:
    """Parse YYYY-MM-DD, DD-MM-YYYY or '12 December 2026'; None when impossible."""
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    else:
        m = re.search(r"\b(\d{2})-(\d{2})-(\d{4})\b", text)
        if m:
            d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        else:
            m = re.search(rf"\b(\d{{1,2}})\s+({_MONTH_ALT})\s+(\d{{4}})\b", text, re.IGNORECASE)
            if m:
                d, mo, y = int(m.group(1)), _MONTHS[m.group(2).lower()], int(m.group(3))
            else:
                m = re.search(rf"\b({_MONTH_ALT})\s+(\d{{1,2}}),?\s+(\d{{4}})\b", text, re.IGNORECASE)
                if not m:
                    return None
                mo, d, y = _MONTHS[m.group(1).lower()], int(m.group(2)), int(m.group(3))
    try:
        return date(y, mo, d)
    except ValueError:
        return None


def find_dates(text: str) -> list[str]:
    """All date-shaped strings in the text, valid or not."""
    found = re.findall(r"\d{4}-\d{2}-\d{2}", text)
    found += re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)
    found += re.findall(rf"\b\d{{1,2}}\s+(?:{_MONTH_ALT})\s+\d{{4}}\b", text, re.IGNORECASE)
    found += re.findall(rf"\b(?:{_MONTH_ALT})\s+\d{{1,2}},?\s+\d{{4}}\b", text, re.IGNORECASE)
    return found
