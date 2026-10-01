"""Deterministic teaching fixture for Capstone Architecture Review."""

def assess(state):
    return {"status": state.get("status", "unknown"), "evidence": state.get("evidence", [])}
