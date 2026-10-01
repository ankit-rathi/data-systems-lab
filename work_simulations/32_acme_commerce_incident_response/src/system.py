"""Deterministic teaching fixture for Incident Response, Rollback & Recovery."""

def assess(state):
    return {"status": state.get("status", "unknown"), "evidence": state.get("evidence", [])}
