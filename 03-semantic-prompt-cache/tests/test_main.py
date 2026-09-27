from src.main import SemanticPromptCache, Request


def test_03_semantic_prompt_cache_accepts_request():
    result = SemanticPromptCache().execute(Request("test-1", {"message": "hello"}))
    assert result.request_id == "test-1"
    assert result.metadata["status"] == "ok"
