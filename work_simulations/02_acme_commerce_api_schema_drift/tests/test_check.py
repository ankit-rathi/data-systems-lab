import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"src"))
from check import non_empty
def test_fixture_is_actionable(): assert non_empty("fixture")
