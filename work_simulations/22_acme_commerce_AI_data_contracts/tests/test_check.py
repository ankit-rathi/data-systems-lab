import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"src"))
from check import bounded
def test_action_boundary(): assert len(bounded([1,2,3]))==2
