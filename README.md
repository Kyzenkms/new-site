# StudyPilot

I built this for my first-semester exams. My notes are a mess - seven
subjects, some typed, some copied from friends, dates all over the place.
StudyPilot reads the folder, works out what has to be revised by when,
and gives me a plan I can actually follow, plus flashcards and a quiz
for each day, made only from my own notes.

Built for the Agentware hackathon, 27-30 Nov 2026. Python, one
dependency (PyMuPDF). The model is Google Gemini by default; any
OpenAI-compatible endpoint works too (see `.env.example`).

## What it does

- Reads notes (`.md`, `.txt`, `.pdf`, `.json`, `.csv`, `.html`) from an
  inbox folder. Nothing outside that folder is ever read.
- Builds a day-by-day plan up to each subject's own exam date - my IKS
  paper is 7 Dec and CFT is 19 Dec, so IKS topics stop on the 6th while
  CFT keeps going. Subjects are mixed across each day, not done one at
  a time.
- Generates today's revision pack (flashcards + MCQ quiz) from the
  sections of my notes that match today's topics. If a section is not
  in my notes, the pack says so instead of making something up.
- Tracks progress. I mark a day done, and if I miss days, the next run
  reshuffles whatever is left into the days remaining.
- Writes a trace of everything it read and decided, so I can check its
  work afterwards.

## The part I cared about: it does not obey the notes

Notes from the internet and group chats can contain text that talks to
an AI - "ignore your instructions", "delete this folder", hidden in
invisible characters or in a web page's image alt text. StudyPilot
treats every file as data:

- Invisible/zero-width characters are stripped before anything is read.
- Instruction-shaped lines are removed and logged. The file itself is
  never deleted, and a file that merely *discusses* these attacks is
  processed normally.
- HTML is reduced to the text a person would actually see. Alt text,
  comments and invisible blocks never reach the agent.
- Broken data is reported, not silently fixed: truncated JSON is
  salvaged record-by-record and the bad fields are listed by name
  (duplicate ids, a year written as `20O4`, a paper dated 2031).
  Impossible dates like 30 February are flagged, never planned around.
- Dates written the way people actually write them - "the fourth of
  December", `07/12/2026`, "Dec 7" - are understood.
- My exam date outranks any date in the notes. Conflicts are flagged
  in the report, not silently resolved.
- If something needed is missing or contradictory, it stops and asks
  (see `output/QUESTIONS.md`) instead of guessing.

## Kill switch and limits

Drop a file named `STOP` into the inbox or output folder and the run
halts at the next step. A step budget caps how much work one run can
do. The agent can only read the inbox, only write the output folder,
and it never deletes anything, anywhere.

## Run it

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # add your Gemini API key; never commit .env
cp /path/to/notes/*.md inbox/
python3 agent.py --inbox inbox --output output \
    --exam-dates "IKS=2026-12-07,LAS=2026-12-09,PPS=2026-12-11"
python3 agent.py --mark-done 2026-11-28   # after finishing a day
```

Outputs: `plan.md`, `packs/<date>.md`, `ingest-report.md`,
`trace.jsonl`, `progress.json`, and `QUESTIONS.md` when it stops to ask.

## Tests

```bash
python -m unittest discover -s tests -v
```

Trap Pack results: `tests/trap-pack/RESULTS.md`.

## Layout

- `agent.py` - the run loop: ingest, stop-and-ask, plan, pack, progress
- `planner.py` - topics from the notes' own headings; the plan arithmetic
- `packs.py` - flashcards + quiz generation, grounded in the notes
- `safety.py` - sanitising, date parsing and validation
- `tools.py` - the agent's only hands: scoped reads/writes, model calls
- `trace.py` - the audit trail (secrets redacted)
