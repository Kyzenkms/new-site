#!/usr/bin/env bash
# One-command demo: real first-semester notes (with three planted trap
# files mixed in), real exam dates. No API key needed for the plan;
# add one to .env and the daily pack is generated too.
set -e
cd "$(dirname "$0")"
rm -rf demo-run
mkdir -p demo-run/inbox
cp demo/inbox/* demo-run/inbox/
python3 agent.py --inbox demo-run/inbox --output demo-run/output \
    --start-date 2026-11-28 \
    --exam-dates "IKS=2026-12-07,LAS=2026-12-09,PPS=2026-12-11,EP=2026-12-15,ICDE=2026-12-17,CFT=2026-12-19"
echo
echo "--- ingest report (traps stripped, conflicts flagged) ---"
cat demo-run/output/ingest-report.md
echo "--- plan (first 2 days) ---"
sed -n '1,30p' demo-run/output/plan.md
