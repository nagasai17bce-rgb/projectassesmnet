from src.main import TokenBudgetOptimizer, Request


def test_05_token_budget_optimizer_accepts_request():
    result = TokenBudgetOptimizer().execute(Request("test-1", {"message": "hello"}))
    assert result.request_id == "test-1"
    assert result.metadata["status"] == "ok"
