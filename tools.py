"""Tools: the agent's only hands, scoped hard.

- Reads happen ONLY inside the inbox folder.
- Writes happen ONLY inside the output folder.
- Nothing is ever deleted, anywhere.
- The only network call is the model API (Gemini), with retry + backoff.
"""
from __future__ import annotations

import csv
import io
import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

SUPPORTED = {".txt", ".md", ".pdf", ".json", ".csv", ".html", ".htm"}


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


class _VisibleText(HTMLParser):
    """Collects only what a reader would actually see on the page.

    Attributes are never collected, so text hidden in an img alt or a
    meta tag (Trap Pack #09) cannot reach the agent; elements styled
    invisible (display:none, font-size:0, ...) are skipped with their
    whole subtree, and comments/scripts/styles are dropped.
    """

    _SKIP = {"script", "style", "noscript", "head", "title", "template"}
    _VOID = {"meta", "link", "img", "br", "hr", "input", "source", "wbr",
             "col", "area", "base", "embed", "track", "param"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._stack: list[bool] = []

    def _hidden(self, tag: str, attrs) -> bool:
        a = dict(attrs)
        if tag in self._SKIP or "hidden" in a:
            return True
        style = a.get("style", "").replace(" ", "").lower()
        return any(h in style for h in (
            "display:none", "visibility:hidden", "font-size:0",
            "width:0", "height:0", "opacity:0"))

    def handle_starttag(self, tag, attrs):
        if tag not in self._VOID:  # void elements never get an end tag
            self._stack.append(self._hidden(tag, attrs))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if self._stack:
            self._stack.pop()

    def handle_data(self, data):
        if not any(self._stack) and data.strip():
            self.parts.append(data.strip())


def extract_html_text(html: str) -> str:
    parser = _VisibleText()
    parser.feed(html)
    return "\n".join(parser.parts)


class Toolbox:
    def __init__(self, inbox: Path, output: Path):
        self.inbox = Path(inbox).resolve()
        self.output = Path(output).resolve()
        self.output.mkdir(parents=True, exist_ok=True)
        self.last_problems: list[str] = []

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
        self.last_problems = []
        meta: dict = {"encoding": None, "pages": None, "json_error": None}
        if suffix == ".pdf":
            text = self._read_pdf(path)
            meta["pages"] = text[1]
            text = text[0]
        else:
            text, meta["encoding"] = decode_tolerant(raw)
            if suffix in (".html", ".htm"):
                text = extract_html_text(text)
            elif suffix == ".json":
                self.last_problems = self._check_json(text)
                if self.last_problems and "does not parse" in self.last_problems[0]:
                    meta["json_error"] = self.last_problems[0]
            elif suffix == ".csv":
                self.last_problems = self._check_csv(text)
        if not text.strip():
            raise NoteError("no extractable text")
        return text, meta

    # ---- broken-data checks: report specifics, never silently pass ----
    def _check_json(self, text: str) -> list[str]:
        try:
            data = json.loads(text)
            records = data if isinstance(data, list) else []
            return self._validate_records(records)
        except json.JSONDecodeError as e:
            # Salvage: any complete {...} object that parses and carries
            # an id is a recovered record, even inside a truncated outer
            # container. Objects nested inside a recovered one are dropped.
            spans, stack = [], []
            for i, ch in enumerate(text):
                if ch == "{":
                    stack.append(i)
                elif ch == "}" and stack:
                    start = stack.pop()
                    try:
                        obj = json.loads(text[start:i + 1])
                    except json.JSONDecodeError:
                        continue
                    if isinstance(obj, dict) and "id" in obj:
                        spans.append((start, i + 1, obj))
            spans.sort(key=lambda s: s[1] - s[0], reverse=True)
            salvaged, kept = [], []
            for start, end, obj in spans:
                if any(start >= ks and end <= ke for ks, ke in kept):
                    continue
                kept.append((start, end))
                salvaged.append(obj)
            problems = [f"JSON does not parse ({e.msg} at line {e.lineno}); "
                        f"recovered {len(salvaged)} complete record(s), "
                        "the rest is truncated or malformed"]
            return problems + self._validate_records(salvaged)

    @staticmethod
    def _validate_records(records: list) -> list[str]:
        problems, ids = [], {}
        this_year = date.today().year
        for rec in records:
            if not isinstance(rec, dict):
                continue
            rid = rec.get("id")
            if rid is not None:
                ids[rid] = ids.get(rid, 0) + 1
            for key, val in rec.items():
                if "year" in str(key).lower():
                    s = str(val)
                    if not (s.isdigit() and len(s) == 4):
                        problems.append(f"record {rid}: bad year value {val!r}")
                    elif int(s) > this_year + 1:
                        problems.append(
                            f"record {rid}: publication year {s} is in the future")
        for rid, n in ids.items():
            if n > 1:
                problems.append(f"duplicate id: {rid} appears {n} times")
        return problems[:8]

    @staticmethod
    def _check_csv(text: str) -> list[str]:
        rows = list(csv.reader(io.StringIO(text)))
        if len(rows) < 2:
            return []
        problems = []
        width = len(rows[0])
        ragged = [i + 1 for i, r in enumerate(rows) if len(r) != width]
        if ragged:
            problems.append(f"{len(ragged)} row(s) have the wrong number of "
                            f"columns (first at line {ragged[0]})")
        seen: dict[str, int] = {}
        for i, r in enumerate(rows[1:], start=2):
            if r and r[0]:
                if r[0] in seen:
                    problems.append(f"duplicate id in column 1: {r[0]} "
                                    f"(lines {seen[r[0]]} and {i})")
                    break
                seen[r[0]] = i
        for i, r in enumerate(rows[1:], start=2):
            for cell in r:
                if cell and re.fullmatch(r"\d{4}-\d{2}-\d{2}", cell):
                    y, mo, d = (int(x) for x in cell.split("-"))
                    try:
                        date(y, mo, d)
                    except ValueError:
                        problems.append(f"impossible date {cell} at line {i}")
        return problems[:8]

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
    _last_call = 0.0

    def call_model(self, prompt: str, max_tokens: int = 2048) -> str:
        """One model call with retry + backoff.

        Two providers, chosen by env: MODEL_API_KEY set -> any
        OpenAI-compatible endpoint (MODEL_BASE_URL, MODEL_NAME);
        otherwise GEMINI_API_KEY -> Google Gemini.

        Calls are paced: the Gemini free tier allows 5 requests/minute
        on this key, and a 7-subject pack fires 7 calls back to back -
        without pacing the whole pack died on HTTP 429 (found by the
        demo recording, 28 Nov). MODEL_MIN_INTERVAL overrides the gap.
        """
        gap = float(os.environ.get("MODEL_MIN_INTERVAL", "13"))
        wait = Toolbox._last_call + gap - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        try:
            if os.environ.get("MODEL_API_KEY", "").strip():
                return self._call_openai_compatible(prompt, max_tokens)
            return self._call_gemini(prompt, max_tokens)
        finally:
            Toolbox._last_call = time.monotonic()

    def _call_openai_compatible(self, prompt: str, max_tokens: int) -> str:
        key = os.environ["MODEL_API_KEY"].strip()
        base = os.environ.get("MODEL_BASE_URL", "https://agentrouter.org/v1").rstrip("/")
        model = os.environ.get("MODEL_NAME", "").strip()
        if not model:
            raise ModelError("MODEL_NAME is not set for the OpenAI-compatible provider")
        body = json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens, "temperature": 0.4,
        }).encode()
        return self._post(f"{base}/chat/completions", body,
                          {"Authorization": f"Bearer {key}"},
                          lambda d: d["choices"][0]["message"]["content"])

    def _call_gemini(self, prompt: str, max_tokens: int) -> str:
        key = os.environ.get("GEMINI_API_KEY", "").strip()
        if not key:
            raise ModelError("GEMINI_API_KEY is not set")
        model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        body = json.dumps({
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": max_tokens, "temperature": 0.4},
        }).encode()
        return self._post(url, body, {"x-goog-api-key": key},
                          lambda d: "".join(
                              p.get("text", "")
                              for p in d["candidates"][0]["content"]["parts"]))

    @staticmethod
    def _post(url: str, body: bytes, headers: dict, extract) -> str:
        last_err = None
        wait = 0.0
        for _ in range(4):
            if wait:
                time.sleep(wait)
            req = urllib.request.Request(
                url, data=body, method="POST",
                headers={"Content-Type": "application/json", **headers})
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    return extract(json.loads(resp.read().decode()))
            except urllib.error.HTTPError as e:
                last_err = e
                wait = 20.0 if e.code == 429 else 3.0  # quota: back right off
            except (urllib.error.URLError, KeyError, IndexError, TimeoutError) as e:
                last_err = e
                wait = 3.0
        raise ModelError(f"model call failed after retries: {type(last_err).__name__}")
