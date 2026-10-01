from src.system import assess
def test_fixture_is_deterministic():
    out=assess({"status":"ok","evidence":["requirements"]})
    assert out["status"]=="ok" and out["evidence"]==["requirements"]
