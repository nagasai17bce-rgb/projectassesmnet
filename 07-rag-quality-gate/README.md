# RAG Quality Gate

> Production-shaped portfolio project by Naga Sai.

## Problem

Offline evaluation service for retrieval recall, groundedness, citation coverage and answer relevance.

## Engineering focus

This project is designed around the kind of production concerns that appear in modern AI/data platforms: explicit interfaces, failure handling, evaluation, observability, cost/latency trade-offs and safe deployment.

## Architecture

```
Client
  |
  v
API / Orchestrator
  |
  +--> Core RAG Quality Gate
  |       |
  |       +--> policies / validation
  |       +--> tools / data
  |       +--> telemetry
  |
  +--> evaluation + audit
```

## Stack

Python, pytest, evaluation

## Run

```bash
python -m src.main
```

The reference implementation intentionally keeps external integrations behind interfaces so they can be replaced with real providers.

## Production hardening

- Add authentication and authorization at the API boundary.
- Add timeouts, retries and circuit breakers around remote dependencies.
- Emit structured traces with request, model/tool, latency and cost metadata.
- Add deterministic regression datasets and CI evaluation gates.
- Add load tests and SLO dashboards before production deployment.

## Why this project exists

This is a portfolio-grade systems exercise, not a claim of production deployment or customer usage.
