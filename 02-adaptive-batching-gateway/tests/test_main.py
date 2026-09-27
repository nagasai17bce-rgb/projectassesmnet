from src.main import AdaptiveBatchingGateway, Request


def test_02_adaptive_batching_gateway_accepts_request():
    result = AdaptiveBatchingGateway().execute(Request("test-1", {"message": "hello"}))
    assert result.request_id == "test-1"
    assert result.metadata["status"] == "ok"
