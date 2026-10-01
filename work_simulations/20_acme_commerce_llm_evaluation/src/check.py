import csv
from pathlib import Path
rows=list(csv.DictReader((Path(__file__).parents[1]/"data"/"eval_cases.csv").open()))
assert {r["type"] for r in rows}=={"refund","shipping","payment","ambiguous"}
assert any(r["expected"]=="needs_review" for r in rows)
print("evaluation set includes ambiguity and escalation")
