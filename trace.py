"""Audit trail: every run appends JSONL events to trace.jsonl.

Each event records what the agent saw, decided, called and got back.
Secrets are redacted before anything is written: the configured API key
and anything that looks like a key/token assignment never reaches disk.
"""
from __future__ import annotations

import json
import re
import time
import uuid
from pathlib import Path

_SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*\S+"),
    re.compile(r"AIza[0-9A-Za-z_\-]{20,}"),  # Google API key shape
]


def redact(text: str, secrets: list[str]) -> str:
    out = text
    for s in secrets:
        if s:
            out = out.replace(s, "[REDACTED]")
    for pat in _SECRET_PATTERNS:
        out = pat.sub(lambda m: m.group(0).split("=")[0].split(":")[0] + "=[REDACTED]", out)
    return out


class Trace:
    def __init__(self, path: Path, secrets: list[str] | None = None):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.run_id = uuid.uuid4().hex[:8]
        self.secrets = secrets or []
        self.events = 0

    def log(self, event: str, **fields) -> None:
        record = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "run": self.run_id,
            "event": event,
        }
        for k, v in fields.items():
            if isinstance(v, str):
                v = redact(v, self.secrets)
            record[k] = v
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        self.events += 1
