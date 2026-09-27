# Tool Routing Agent

Chooses among APIs and data tools using structured tool schemas and confidence thresholds.

## Architecture
Client → agent/API → policy + tool router → retrieval/tools → response + trace.

## Production concerns
- typed tool contracts and validation
- timeouts, retries and authorization
- audit trail for every tool call
- offline evaluation dataset
- latency/cost telemetry

## Run
See `src/main.py`. External providers are intentionally behind interfaces.

Portfolio systems exercise; no unverified production claims.