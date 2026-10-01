import csv
from pathlib import Path
rows=list(csv.DictReader((Path(__file__).parents[1]/"data"/"requests.csv").open()))
assert rows and all(int(r["input_tokens"])>0 for r in rows)
assert all(int(r["latency_ms"])>0 for r in rows)
print("model boundary records are present")
