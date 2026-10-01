from collections import Counter
from pathlib import Path
import csv

ROOT = Path(__file__).parents[1]
rows = list(csv.DictReader((ROOT / "data" / "events.csv").open()))

# This helper intentionally does not declare a root cause.
# Learners should use it to inspect the evidence and build their own diagnosis.
print("events:", len(rows))
print("customers:", Counter(r["customer_id"] for r in rows))
print("max event-to-processing delay:", max(int(r["processing_time"]) - int(r["event_time"]) for r in rows))
