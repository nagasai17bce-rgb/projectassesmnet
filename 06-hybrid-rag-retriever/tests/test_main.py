from src.main import HybridRAGRetriever, Request


def test_06_hybrid_rag_retriever_accepts_request():
    result = HybridRAGRetriever().execute(Request("test-1", {"message": "hello"}))
    assert result.request_id == "test-1"
    assert result.metadata["status"] == "ok"
