import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"src"))
from check import is_stale
def test_stale_read_is_detected(): assert is_stale(10,9) and not is_stale(10,10)
