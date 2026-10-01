from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from check import load_rows, validate_snapshot

def test_fixture_is_deterministic_and_schema_is_explicit():
    rows=load_rows(Path(__file__).resolve().parents[1]/"data"/"customer_snapshots.csv")
    assert len(rows)==4
    assert validate_snapshot(rows)
