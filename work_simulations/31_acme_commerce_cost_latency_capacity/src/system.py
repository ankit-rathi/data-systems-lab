"""Deterministic teaching fixture for Cost, Latency & Capacity Planning."""

def assess(state):
    return {"status": state.get("status", "unknown"), "evidence": state.get("evidence", [])}
