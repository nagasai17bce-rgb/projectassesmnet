from src.main import LLMInferenceRouter, Request


def test_01_llm_inference_router_accepts_request():
    result = LLMInferenceRouter().execute(Request("test-1", {"message": "hello"}))
    assert result.request_id == "test-1"
    assert result.metadata["status"] == "ok"
