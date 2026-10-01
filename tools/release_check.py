"""Run the local release gate for Data & AI Engineering Lab.

The gate intentionally stays standard-library/process based so it can run in
Colab, CI, or a normal clone without a project-specific test framework.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run(label: str, args: list[str], env: dict[str, str] | None = None) -> None:
    print(f"\n=== {label} ===", flush=True)
    proc = subprocess.run(args, cwd=ROOT, env=env, text=True)
    if proc.returncode:
        raise SystemExit(proc.returncode)


run("Build GitHub Pages source", [PYTHON, "tools/build_site.py"])
run("Repository validation", [PYTHON, "tools/validate_repo.py"])
run("Content quality gate", [PYTHON, "tools/quality_check.py"])
run("Curriculum graph validation", [PYTHON, "tools/validate_graph.py"])
run("Link and release-integrity validation", [PYTHON, "tools/validate_links.py"])
run("Portfolio template validation", [PYTHON, "tools/validate_portfolio.py"])
run("Notebook structural smoke", [PYTHON, "tools/smoke_notebooks.py"])
print('\nApprenticeship scenario tests: run `python tools/run_scenarios.py` as the separate release test step.')

# The final gate checks for any generated artifacts left by other tooling.
for name in (".pytest_cache", "__pycache__", ".ipynb_checkpoints"):
    found = list(ROOT.rglob(name))
    if found:
        print(f"RELEASE CHECK FAILED: generated artifacts found: {found}")
        raise SystemExit(1)

# GitHub Actions has the authoritative Jekyll build. Locally, run it when the
# executable is installed; otherwise make the environment limitation explicit.
jekyll = shutil.which("jekyll")
if jekyll:
    run("Jekyll build", [jekyll, "build", "--source", "site", "--destination", "/tmp/data-systems-lab-site"])
else:
    print("\nJekyll build: SKIPPED (jekyll executable is not installed locally; GitHub Pages CI remains the authoritative renderer).")

print("\nRELEASE CHECK PASSED")
