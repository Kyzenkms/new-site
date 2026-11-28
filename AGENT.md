# AGENT.md - StudyPilot

## What it is

An unattended revision agent. Input: a folder of study notes and the
student's exam date(s). Output: a day-by-day revision plan, a daily
flashcard + quiz pack generated only from those notes, an ingest
report, and a full audit trace. It runs to completion on its own; when
material is missing, broken or contradictory it stops and asks
(`output/QUESTIONS.md`, exit code 2) instead of inventing.

## Autonomy loop

1. List the inbox (scoped read - nothing outside it is ever opened).
2. Read and sanitise each file; quarantine the unusable, flag the broken.
3. Resolve exam dates: the user's word first, per-subject dates
   supported; note dates are evidence, never orders.
4. Build the plan deterministically (no model calls - it is arithmetic
   over the notes' own headings, so it can be checked).
5. Generate today's pack with the model, grounded in the note sections
   matching today's topics.
6. Record progress; on the next run, finished topics drop out and the
   rest is reshuffled into the days left (missed-day recovery).

Every step checks the kill switch and the step budget first.

## Tools

The agent's only hands are in `tools.py`:

- `list_inbox` / `read_note` - reads, inbox only. PDF via PyMuPDF;
  HTML reduced to visible text; tolerant decoding (UTF-8, then
  Windows-1252); JSON salvage and CSV sanity checks that report bad
  records by name instead of dropping them.
- `write_output` - writes, output folder only. Nothing is ever deleted.
- `call_model` - the only network call. Gemini by default
  (`GEMINI_API_KEY`, model `gemini-2.5-flash`); any OpenAI-compatible
  endpoint via `MODEL_API_KEY` / `MODEL_BASE_URL` / `MODEL_NAME`.
  Calls are paced (default 13s apart, `MODEL_MIN_INTERVAL`) to live
  inside free-tier quotas - the Gemini free tier caps requests per
  minute and per day per model - and a 429 gets a long backoff
  instead of the standard retry.

## Guardrails

- Notes are data, never instructions: zero-width characters stripped,
  instruction-shaped lines removed and logged, flag-and-continue (a
  file quoting an attack is processed normally).
- HTML alt text, comments and invisible elements are never extracted.
- Impossible dates are flagged as broken data, never planned around;
  the user's exam date outranks note dates; conflicts are reported.
- Grounding: packs are generated only from the student's own note
  sections; a failed generation is reported with the topics listed,
  never filled with invented content.
- Secrets are redacted from the trace, including anything shaped like
  an API key.

## Kill switch and budget

A file named `STOP` in the inbox or output folder halts the run at the
next step (exit code 3, `killed` event in the trace). `--max-steps`
(default 200) caps the work one run can do.

## Exit codes

- `0` - plan (and pack, when a model key is configured) written
- `2` - stopped to ask; see `output/QUESTIONS.md`
- `3` - halted by the STOP file or the step budget

## Failure behaviour

Per-file failures never crash the run: unreadable files are
quarantined with a reason, broken records are listed in
`ingest-report.md`, and a failed model call degrades that subject's
pack section to a topic list. Everything is in `trace.jsonl`.
