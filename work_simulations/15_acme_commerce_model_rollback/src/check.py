from pathlib import Path
import csv

def load_rows(path):
    with Path(path).open() as f:
        return list(csv.DictReader(f))

def validate_snapshot(rows):
    required={"customer_id","snapshot_date","orders_30d","days_since_last_order","churned"}
    assert required <= set(rows[0])
    assert len({r["customer_id"] for r in rows}) == len(rows)
    return True
