"""Deterministic teaching fixture for Reliability, SLOs & Failure Budgets."""

def assess(state):
    return {"status": state.get("status", "unknown"), "evidence": state.get("evidence", [])}
