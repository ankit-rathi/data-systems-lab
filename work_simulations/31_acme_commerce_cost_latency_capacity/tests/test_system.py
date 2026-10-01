from src.system import assess
def test_capacity_review_has_both_cost_and_latency():
    out=assess({"status":"review","evidence":["p95","cost"]})
    assert set(["p95","cost"])<=set(out["evidence"])
