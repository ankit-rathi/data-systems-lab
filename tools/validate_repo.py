"""Lightweight repository validator for the Data & AI Engineering Lab.

Run from the repository root:
    python tools/validate_repo.py

Standard library only.
"""
from __future__ import annotations

import ast
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


# 1. Notebook JSON + Python compilation + sketch-note convention.
notebooks = sorted(ROOT.glob("**/*.ipynb"))
for path in notebooks:
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path}: invalid JSON: {exc}")
        continue
    if nb.get("nbformat", 0) < 4:
        fail(f"{path}: unsupported notebook format")
    cells = nb.get("cells", [])
    if not cells or cells[0].get("cell_type") != "markdown":
        fail(f"{path}: first cell must be markdown")
    early = "\n".join("".join(c.get("source", [])) for c in cells[:4])
    if "Sketch note" not in early and "Sketch note" not in early.lower():
        fail(f"{path}: missing opening sketch-note section")

    for i, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        try:
            ast.parse(source, filename=f"{path}:cell-{i}")
        except SyntaxError as exc:
            # Colab/Jupyter magics are valid notebook syntax but not Python AST.
            if any(line.lstrip().startswith(("%", "!")) for line in source.splitlines()):
                continue
            fail(f"{path}:cell-{i}: Python syntax error: {exc}")

# 2. Every substantial notebook must point to its own sketch-note asset.
for path in notebooks:
    if "99_templates" in path.parts:
        continue
    cells = json.loads(path.read_text(encoding="utf-8")).get("cells", [])
    markdown = "\n".join("".join(c.get("source", [])) for c in cells if c.get("cell_type") == "markdown")
    refs = re.findall(r"!\[[^]]*\]\(([^)]+)\)", markdown)
    refs = [r for r in refs if "sketch-notes/" in r]
    if not refs:
        fail(f"{path}: missing sketch-note image reference")
    else:
        ref = refs[0]
        if "_placeholder.svg" in ref:
            fail(f"{path}: placeholder sketch-note is not allowed")
        if not (path.parent / ref).exists():
            fail(f"{path}: sketch-note asset does not exist: {ref}")

# 3. Manifest coverage and paths.
manifest = ROOT / "NOTEBOOK_MANIFEST.csv"
if not manifest.exists():
    fail("NOTEBOOK_MANIFEST.csv is missing")
else:
    with manifest.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    manifest_paths = {r["path"] for r in rows}
    actual_paths = {str(p.relative_to(ROOT)).replace("\\", "/") for p in notebooks if "99_templates" not in p.parts}
    missing = actual_paths - manifest_paths
    stale = manifest_paths - actual_paths
    for p in sorted(missing):
        fail(f"manifest: notebook missing from manifest: {p}")
    for p in sorted(stale):
        fail(f"manifest: path does not exist: {p}")

# 4. README local links (skip external URLs and planned textual paths).
readme = ROOT / "README.md"
if readme.exists():
    text = readme.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        candidate = (ROOT / target.split("#", 1)[0]).resolve()
        if not candidate.exists():
            fail(f"README: broken local link: {target}")

# 5. Colab link shape for direct notebook links.
if readme.exists():
    text = readme.read_text(encoding="utf-8")
    for url in re.findall(r"https://colab\.research\.google\.com/[^)\s]+", text):
        if "research.google.com/colab/" in url and "/github/ankit-rathi/data-systems-lab/blob/main/" not in url:
            fail(f"README: unexpected Colab URL: {url}")

# 6. README is intentionally concise in v1.4; notebook-by-notebook Colab links live on Pages.
if readme.exists():
    text = readme.read_text(encoding="utf-8")
    if "ankit-rathi/data-ai-engineering-lab" in text:
        fail("README: stale repository slug found in Colab links")
    if "00–54" not in text:
        fail("README: current 00–54 curriculum range is missing")

# 7. GitHub Pages source must be generated and point notebook links to the source repository.
site_index = ROOT / "site" / "index.md"
site_builder = ROOT / "tools" / "build_site.py"
if not site_builder.exists():
    fail("GitHub Pages builder tools/build_site.py is missing")
if not site_index.exists():
    fail("GitHub Pages generated site/index.md is missing; run python tools/build_site.py")
elif "github.com/ankit-rathi/data-systems-lab/blob/main/" not in site_index.read_text(encoding="utf-8"):
    fail("GitHub Pages index does not contain repository links for notebook sources")

# 8. Work simulation checks.
scenario = ROOT / "work_simulations" / "01_acme_commerce_revenue_mismatch"
for required in ["README.md", "WORK_SIMULATION.md", "ticket.md", "evidence.md", "data/orders.csv", "data/payments.csv", "src/revenue_report.sql", "tests/test_revenue.py"]:
    if not (scenario / required).exists():
        fail(f"work simulation: missing required file: {required}")

# 9. Agent Workbench baseline.
for name in [
    'agent_lab/README.md',
    'agent_lab/context/agent_work_contract.md',
    'agent_lab/tools/tool_gateway.py',
    'agent_lab/policies/permissions.json',
    'agent_lab/traces/example_trace.json',
    'agent_lab/evals/cases.json',
    'agent_lab/graders/grade_trace.py',
]:
    if not (ROOT / name).exists():
        fail(f'agent workbench artifact missing: {name}')

# 10. Learner portfolio template.
for name in ['portfolio_template/README.md','portfolio_template/evidence_record.json']:
    if not (ROOT/name).exists(): fail(f'portfolio template missing: {name}')
for name in ['01_requirements','02_architecture','03_data_contracts','04_experiments','05_incidents','06_agent_work','07_decisions','08_evals','09_production_defense']:
    if not (ROOT/'portfolio_template'/name).is_dir(): fail(f'portfolio template directory missing: {name}')

# 11. Learner exercise/reference solution coverage.
solutions = ROOT / "solutions"
if not (solutions / "README.md").exists():
    fail("solutions/README.md is missing")
for n in range(55):
    if not (solutions / "notebooks" / f"{n:02d}.md").exists():
        fail(f"missing notebook reference solution: {n:02d}")
for sid in range(1,34):
    if not (solutions / "scenarios" / f"S{sid:02d}.md").exists():
        fail(f"missing scenario reference solution: S{sid:02d}")

# 12. Required baseline documents.
for name in [
    "LEARNER_GUIDE.md",
    "docs/maintainer/SKETCH_NOTE_STANDARD.md",
    "LEARNER_GUIDE.md",
    "LEARNER_GUIDE.md",
    "docs/maintainer/MODULE_TEMPLATE.md",
    "CONTRIBUTING.md",
    "CONTEXT_HANDOFF.md",
    "docs/maintainer/ROADMAP.md",
    "docs/maintainer/GITHUB_PAGES.md",
    "LEARNER_GUIDE.md",
    "LEARNER_GUIDE.md",
    "EVIDENCE_PORTFOLIO.md",
]:
    if not (ROOT / name).exists():
        fail(f"required baseline document missing: {name}")

print(f"Checked {len(notebooks)} notebooks.")
if errors:
    print("\nVALIDATION FAILED")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)
print("VALIDATION PASSED")
