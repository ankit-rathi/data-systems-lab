import csv
from pathlib import Path
rows=list(csv.DictReader((Path(__file__).parents[1]/"data"/"tool_requests.csv").open()))
allowed={"lookup_order","lookup_refund"}
assert any(r["tool"]=="delete_order" for r in rows)
assert all(r["tool"] in allowed for r in rows if r["request_id"] in {"T1","T2"})
print("unsafe write tool remains blocked until authorization is designed")
