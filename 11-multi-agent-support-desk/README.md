# Multi-Agent Support Desk

Supervisor agent delegates billing, technical and account workflows to specialist agents.

## Architecture
Request → supervisor/orchestrator → specialist tools → state/memory → evaluator → response.

## Engineering focus
Typed state, deterministic routing, idempotent tools, trace IDs, replayable evaluations and failure recovery.

## Run
`python src/main.py`

Portfolio systems exercise; benchmark claims are intentionally omitted until reproducible tests exist.