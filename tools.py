"""Tools: the agent's only hands, scoped hard.

- Reads happen ONLY inside the inbox folder.
- Writes happen ONLY inside the output folder.
- Nothing is ever deleted, anywhere.
- The only network call is the model API (Gemini), with retry + backoff.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

SUPPORTED = {".txt", ".md", ".pdf", ".json", ".csv"}


class NoteError(Exception):
    """A note that cannot be read: corrupt, empty, or unsupported."""


class ModelError(Exception):
    """The model API failed after retries, or no key is configured."""


def decode_tolerant(raw: bytes) -> tuple[str, str]:
    """UTF-8 first, Windows-1252 fallback (Trap Pack #07 lies about encoding)."""
    try:
        return raw.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        return raw.decode("cp1252", errors="replace"), "cp1252(fallback)"


class Toolbox:
    def __init__(self, inbox: Path, output: Path):
        self.inbox = Path(inbox).resolve()
        self.output = Path(output).resolve()
        self.output.mkdir(parents=True, exist_ok=True)

    # ---- reads ------------------------------------------------------
    def list_inbox(self) -> list[Path]:
        if not self.inbox.is_dir():
            return []
        return sorted(
            p for p in self.inbox.iterdir()
            if p.is_file() and not p.name.startswith(".")
        )

    def read_note(self, path: Path) -> tuple[str, dict]:
        """Extract text from one inbox file. Raises NoteError on bad input."""
        path = Path(path).resolve()
        if self.inbox not in path.parents:
            raise NoteError(f"refused: {path.name} is outside the inbox")
        suffix = path.suffix.lower()
        if suffix not in SUPPORTED:
            raise NoteError(f"unsupported file type: {suffix or '(none)'}")
        raw = path.read_bytes()
        if not raw.strip():
            raise NoteError("file is empty")
        meta: dict = {"encoding": None, "pages": None, "json_error": None}
        if suffix == ".pdf":
            text = self._read_pdf(path)
            meta["pages"] = text[1]
            text = text[0]
        else:
            text, meta["encoding"] = decode_tolerant(raw)
            if suffix == ".json":
                try:
                    json.loads(text)
                except json.JSONDecodeError as e:
                    meta["json_error"] = f"{e.msg} at line {e.lineno}"
        if not text.strip():
            raise NoteError("no extractable text")
        return text, meta

    @staticmethod
    def _read_pdf(path: Path) -> tuple[str, int]:
        try:
            import pymupdf
        except ImportError as e:
            raise NoteError("pymupdf not installed") from e
        try:
            doc = pymupdf.open(path)
        except Exception as e:
            raise NoteError(f"corrupt PDF: {e}") from e
        pages = [page.get_text() for page in doc]
        return "\n".join(pages), len(pages)

    # ---- writes -----------------------------------------------------
    def write_output(self, name: str, content: str) -> Path:
        target = (self.output / name).resolve()
        if self.output not in target.parents:
            raise NoteError(f"refused: write outside the output folder ({name})")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    # ---- model ------------------------------------------------------
    def call_model(self, prompt: str, max_tokens: int = 2048) -> str:
        key = os.environ.get("GEMINI_API_KEY", "").strip()
        if not key:
            raise ModelError("GEMINI_API_KEY is not set")
        model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        body = json.dumps({
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": max_tokens, "temperature": 0.4},
        }).encode()
        last_err = None
        for attempt, wait in enumerate([0, 2, 5]):
            if wait:
                time.sleep(wait)
            req = urllib.request.Request(
                url, data=body, method="POST",
                headers={"Content-Type": "application/json", "x-goog-api-key": key},
            )
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    data = json.loads(resp.read().decode())
                parts = data["candidates"][0]["content"]["parts"]
                return "".join(p.get("text", "") for p in parts)
            except (urllib.error.URLError, KeyError, IndexError, TimeoutError) as e:
                last_err = e
        raise ModelError(f"model call failed after retries: {type(last_err).__name__}")
