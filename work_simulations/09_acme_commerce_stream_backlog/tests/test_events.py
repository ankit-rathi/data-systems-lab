import csv
from pathlib import Path

DATA = Path(__file__).parents[1] / "data" / "events.csv"


def test_event_ids_are_unique():
    rows = list(csv.DictReader(DATA.open()))
    ids = [r["event_id"] for r in rows]
    assert len(ids) == len(set(ids))


def test_late_event_is_visible_in_raw_data():
    rows = list(csv.DictReader(DATA.open()))
    late = [r for r in rows if int(r["processing_time"]) - int(r["event_time"]) >= 5]
    assert {r["event_id"] for r in late} == {"E003"}
