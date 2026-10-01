import csv
from pathlib import Path
rows=list(csv.DictReader((Path(__file__).parents[1]/"data"/"retrieval_cases.csv").open()))
assert len(rows)==3
assert len({r["expected_source"] for r in rows})==3
print("evaluation cases keep retrieval evidence explicit")
