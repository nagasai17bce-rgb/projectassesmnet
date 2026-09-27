# MCP Enterprise Gateway

Secure MCP tool gateway with allowlists, authentication, audit events and rate limits.

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