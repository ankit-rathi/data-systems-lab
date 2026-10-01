from src.system import assess
def test_failure_evidence_is_preserved():
    out=assess({"status":"degraded","evidence":["error-rate","dependency"]})
    assert out["status"]=="degraded" and len(out["evidence"])==2
