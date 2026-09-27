"""Hybrid RAG Retriever: Combines lexical and vector retrieval, then reranks evidence before generation."""

from dataclasses import dataclass, field
from typing import Any
import time


@dataclass
class Request:
    id: str
    payload: dict[str, Any]
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Result:
    request_id: str
    output: Any
    latency_ms: float
    metadata: dict[str, Any] = field(default_factory=dict)


class HybridRAGRetriever:
    """Small dependency-free core that can be wrapped by FastAPI, workers or jobs."""

    def execute(self, request: Request) -> Result:
        started = time.perf_counter()

        # Replace this deterministic core with the real provider/tool implementation.
        output = self.handle(request)

        return Result(
            request_id=request.id,
            output=output,
            latency_ms=(time.perf_counter() - started) * 1000,
            metadata={"project": "06-hybrid-rag-retriever", "status": "ok"},
        )

    def handle(self, request: Request) -> dict[str, Any]:
        return {
            "accepted": True,
            "request_id": request.id,
            "next_step": "connect_provider_or_tool",
            "input_keys": sorted(request.payload.keys()),
        }


if __name__ == "__main__":
    service = HybridRAGRetriever()
    print(service.execute(Request("demo-1", {"message": "hello"})))
