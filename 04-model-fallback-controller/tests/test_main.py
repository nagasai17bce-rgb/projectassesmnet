from src.main import ModelFallbackController, Request


def test_04_model_fallback_controller_accepts_request():
    result = ModelFallbackController().execute(Request("test-1", {"message": "hello"}))
    assert result.request_id == "test-1"
    assert result.metadata["status"] == "ok"
