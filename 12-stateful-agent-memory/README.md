# Stateful Agent Memory

Conversation state and durable memory with TTL, retrieval, compaction and privacy boundaries.

## Design
Event/request input -> policy layer -> core workflow -> telemetry -> evaluation.

## Production concerns
Typed contracts, failure isolation, retries, observability, reproducible evaluation, CI and deployment gates.

## Implementation plan
1. Build deterministic core.
2. Add provider interfaces.
3. Add integration tests.
4. Add tracing and metrics.
5. Add load tests and benchmark reports.

This is a portfolio systems project; no unverified production metrics are claimed.
