from src.system import assess
def test_audit_actor_is_required():
    out=assess({"status":"blocked","evidence":["actor","policy"]})
    assert "actor" in out["evidence"]
