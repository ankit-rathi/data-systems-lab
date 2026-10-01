from src.system import assess
def test_recovery_evidence_includes_side_effects():
    out=assess({"status":"recovering","evidence":["rollback","side-effects"]})
    assert "side-effects" in out["evidence"]
