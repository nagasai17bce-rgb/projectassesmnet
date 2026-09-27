# SQL Analytics Agent

Plans safe SQL from natural-language questions, validates queries and explains results.

## Architecture
Ingress -> planner/orchestrator -> tools/data -> validation -> structured result.

## Production concerns
Timeout budgets, idempotency, authorization, audit events, tracing, evaluation datasets and rollback paths.

## Implementation milestones
- deterministic core
- provider/tool adapters
- tests and fixtures
- Docker + CI
- load and failure testing

Portfolio systems project; benchmark numbers will only be added after reproducible experiments.
