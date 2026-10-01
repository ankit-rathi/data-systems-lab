import csv
from pathlib import Path
rows=list(csv.DictReader((Path(__file__).parents[1]/"data"/"responses.csv").open()))
assert any(not r["action"] for r in rows), "fixture should contain a malformed response"
valid_actions={"approve","review","reject"}
valid=[r for r in rows if r["action"] in valid_actions and 0<=float(r["confidence"] or -1)<=1]
assert len(valid)==2
print("validator must separate accepted and rejected responses")
