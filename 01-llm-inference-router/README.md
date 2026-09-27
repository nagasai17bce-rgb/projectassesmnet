# LLM Inference Router

> Production-shaped portfolio project by Naga Sai.

## Problem

Routes requests across model backends using latency, token budget, capability and health signals.

## Engineering focus

This project is designed around the kind of production concerns that appear in modern AI/data platforms: explicit interfaces, failure handling, evaluation, observability, cost/latency trade-offs and safe deployment.

## Architecture

```
Client
  |
  v
API / Orchestrator
  |
  +--> Core LLM Inference Router
  |       |
  |       +--> policies / validation
  |       +--> tools / data
  |       +--> telemetry
  |
  +--> evaluation + audit
```

## Stack

FastAPI, Python, Redis, OpenTelemetry

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
