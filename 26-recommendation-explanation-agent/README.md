# Recommendation Explanation Agent

Generates grounded explanations for recommendations using feature and policy context.

## System design
API -> planner -> domain tools/data -> validation -> explanation/result -> trace.

## Engineering depth
Focus on correctness, explainability, deterministic interfaces, failure handling, observability and evaluation rather than a thin chatbot wrapper.

## Next implementation steps
1. Domain model and contracts.
2. Tool adapters.
3. Synthetic dataset and regression suite.
4. API + Docker + CI.
5. Load, failure and cost testing.

Portfolio systems project; no unverified production metrics are claimed.
