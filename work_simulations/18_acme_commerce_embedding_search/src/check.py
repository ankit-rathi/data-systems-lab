import csv
from pathlib import Path
rows=list(csv.DictReader((Path(__file__).parents[1]/"data"/"queries.csv").open()))
assert len(rows)==2
assert rows[0]["expected_policy"]=="refund_policy"
print("fixture exposes a vocabulary mismatch")
