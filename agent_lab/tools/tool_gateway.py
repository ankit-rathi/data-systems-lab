"""Small deterministic tool gateway used by the Agent Workbench exercises."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ToolRequest:
    name: str
    arguments: dict
    permission_level: int
    human_approved: bool = False


READ_ONLY = {"inspect_fixture", "read_trace", "read_policy"}
MUTATING = {"sandbox_write", "run_tests", "create_pr", "deploy_with_approval", "bounded_production_action"}


def authorize(request: ToolRequest) -> dict:
    """Return a deterministic authorization decision; never execute a tool."""
    if request.name in READ_ONLY:
        return {"allowed": request.permission_level >= 1, "reason": "read-only tool"}
    if request.name not in MUTATING:
        return {"allowed": False, "reason": "unknown tool"}
    if request.permission_level < 3:
        return {"allowed": False, "reason": "permission level too low"}
    if request.name in {"deploy_with_approval", "bounded_production_action"} and not request.human_approved:
        return {"allowed": False, "reason": "human approval required"}
    return {"allowed": True, "reason": "policy satisfied"}
