from src.system import assess
def test_capstone_review_requires_operational_evidence():
    out=assess({"status":"review","evidence":["requirements","failure-modes","rollback","security"]})
    assert len(out["evidence"])>=4
