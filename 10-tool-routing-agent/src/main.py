from dataclasses import dataclass
from typing import Any

@dataclass
class Request:
    id: str
    input: dict[str, Any]

class ToolRoutingAgent:
    def run(self, request: Request) -> dict[str, Any]:
        # Replace this boundary with the real model/tool provider.
        return {"request_id": request.id, "accepted": True, "next": "provider_or_tool", "input": request.input}

if __name__ == "__main__":
    print(ToolRoutingAgent().run(Request("demo", {"query": "hello"})))
