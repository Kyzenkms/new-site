# Safety - StudyPilot

## What the agent can touch

- Reads: only the folder given as `--inbox`.
- Writes: only the folder given as `--output`.
- Deletes: nothing, ever. There is no delete code path.
- Network: one call only - the model API (Gemini by default, or an
  OpenAI-compatible endpoint the user configures).

## Notes are data, never instructions

Every input file is treated as hostile until it proves otherwise:

- Invisible and zero-width characters are stripped before reading.
- Lines shaped like instructions to an agent (delete, send, exfiltrate,
  fake a record, echo a secret) are removed and logged in the trace.
  The file is kept; the run continues. A file that merely *discusses*
  attacks is processed normally - flag-and-continue, never
  refuse-on-keywords.
- HTML is reduced to visible text. Alt attributes, comments, meta tags
  and invisible elements are never extracted.
- Broken data is reported with specifics (which record, which field),
  never silently repaired or dropped.

## Dates and facts

- Impossible dates are broken data: flagged, never planned around.
- The user's exam date outranks any date in the notes; conflicts are
  written into the ingest report, not silently resolved.
- Generated content is grounded in the user's own notes. A failed
  generation is reported with its topics listed - never backfilled
  with invented material.

## Stopping

- Kill switch: a file named `STOP` in the inbox or output folder halts
  the run at the next step, mid-work, cleanly (exit code 3).
- Step budget (`--max-steps`, default 200) caps one run's work.
- Stop-and-ask: missing or contradictory essentials produce
  `output/QUESTIONS.md` and exit code 2 instead of a guess.

## Secrets

- API keys live in `.env` (gitignored) or the environment, never in
  the repo, and are redacted from the audit trace - as is anything
  shaped like a key that appears in the input files.
