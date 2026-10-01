from pathlib import Path
import runpy

def test_scenario_18():
    runpy.run_path(str(Path(__file__).parents[1]/"src"/"check.py"))
