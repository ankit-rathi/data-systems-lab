"""Deterministic checks for an agent trace."""
from __future__ import annotations


def grade(trace: dict) -> dict:
    required = {"goal", "context", "proposal", "verification", "decision"}
    present = required.intersection(trace)
    checks = {
        "has_work_contract_fields": present == required,
        "has_verification": bool(trace.get("verification")),
        "decision_is_explicit": trace.get("decision") in {"ship", "revise", "reject", "escalate"},
        "approval_is_recorded": "human_approval" in trace,
    }
    return {"passed": all(checks.values()), "checks": checks}
