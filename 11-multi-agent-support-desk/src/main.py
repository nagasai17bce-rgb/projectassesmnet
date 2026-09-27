from dataclasses import dataclass
from typing import Any

@dataclass
class Task:
    id: str
    payload: dict[str, Any]

class MultiAgentSupportDesk:
    def run(self, task: Task) -> dict[str, Any]:
        return {"task_id": task.id, "route": "supervisor", "status": "accepted", "payload_keys": sorted(task.payload)}

if __name__ == "__main__":
    print(MultiAgentSupportDesk().run(Task("demo", {"query":"hello"})))
