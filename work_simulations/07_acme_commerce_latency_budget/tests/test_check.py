import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"src"))
from check import p95
def test_latency_measurement_is_explicit(): assert p95([38,42,41])==41
