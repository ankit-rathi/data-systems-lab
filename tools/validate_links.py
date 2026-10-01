"""Validate repository-local links and generated GitHub Pages navigation.

Run from the repository root:
    python tools/validate_links.py

The check is intentionally offline: local targets and known GitHub/Colab URL
shapes are validated without depending on network availability.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def local_target(source: Path, target: str) -> Path | None:
    target = target.strip().split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "data:")):
        return None
    if target.startswith("/"):
        return (ROOT / target.lstrip("/")).resolve()
    return (source.parent / target).resolve()


def check_markdown(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        candidate = local_target(path, target)
        if candidate is not None and not candidate.exists():
            # Template placeholders are deliberately documented as examples.
            if target.startswith("path/to/"):
                continue
            fail(f"{path.relative_to(ROOT)}: broken local link: {target}")


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a":
            for key, value in attrs:
                if key.lower() == "href" and value:
                    self.hrefs.append(value)


def check_site() -> None:
    path = ROOT / "site" / "index.md"
    if not path.exists():
        fail("site/index.md is missing")
        return
    text = path.read_text(encoding="utf-8")
    # Generated Pages contains HTML inside Markdown. Validate every anchor.
    parser = AnchorParser()
    parser.feed(text)
    for href in parser.hrefs:
        parsed = urlparse(href)
        if parsed.scheme in {"http", "https"}:
            if parsed.netloc == "github.com":
                expected = "/ankit-rathi/data-systems-lab/"
                if not parsed.path.startswith(expected):
                    fail(f"site/index.md: unexpected GitHub URL: {href}")
                else:
                    # blob/tree targets should point at an actual repository path.
                    parts = parsed.path[len(expected):].split("/")
                    if parts and parts[0] in {"blob", "tree"} and len(parts) >= 3:
                        repo_path = "/".join(parts[2:])
                        candidate = (ROOT / repo_path).resolve()
                        if not candidate.exists():
                            fail(f"site/index.md: GitHub target does not exist: {href}")
            elif parsed.netloc == "colab.research.google.com":
                prefix = "/github/ankit-rathi/data-systems-lab/blob/main/"
                if not parsed.path.startswith(prefix):
                    fail(f"site/index.md: unexpected Colab URL: {href}")
                else:
                    repo_path = parsed.path[len(prefix):]
                    if not (ROOT / repo_path).exists():
                        fail(f"site/index.md: Colab target does not exist: {href}")
            continue
        if href.startswith("#"):
            continue
        candidate = local_target(path, href)
        if candidate is not None and not candidate.exists():
            fail(f"site/index.md: broken local href: {href}")


def check_notebooks() -> None:
    for path in sorted(ROOT.rglob("*.ipynb")):
        if "99_templates" in path.parts:
            continue
        try:
            nb = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue
            text = "".join(cell.get("source", []))
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                candidate = local_target(path, target)
                if candidate is not None and not candidate.exists():
                    fail(f"{path.relative_to(ROOT)}: broken local link: {target}")


def check_apprenticeship_map() -> None:
    map_path = ROOT / "APPRENTICESHIP_NOTEBOOK_MAP.csv"
    if not map_path.exists():
        fail("APPRENTICESHIP_NOTEBOOK_MAP.csv is missing")
        return
    rows = list(csv.DictReader(map_path.open(newline="", encoding="utf-8")))
    scenario_dirs = {
        f"S{int(p.name[:2]):02d}": p
        for p in (ROOT / "work_simulations").iterdir()
        if p.is_dir() and p.name[:2].isdigit()
    }
    for row in rows:
        nb = ROOT / row["notebook_path"]
        if not nb.exists():
            fail(f"map: notebook target does not exist: {row['notebook_path']}")
        for sid in [x.strip() for x in row["apprenticeship_scenarios"].split(",") if x.strip().startswith("S")]:
            if sid not in scenario_dirs:
                fail(f"map: {row['notebook']} points to missing scenario {sid}")


def check_generated_artifacts() -> None:
    generated = []
    for name in (".pytest_cache", "__pycache__", ".ipynb_checkpoints"):
        generated.extend(ROOT.rglob(name))
    unique = sorted({p.resolve() for p in generated if p.exists()})
    if unique:
        for p in unique:
            try:
                rel = p.relative_to(ROOT)
            except ValueError:
                rel = p
            fail(f"release artifact must not be packaged: {rel}")


for md in sorted(ROOT.rglob("*.md")):
    if ".git" not in md.parts and "site" not in md.parts:
        check_markdown(md)
check_notebooks()
check_site()
check_apprenticeship_map()
check_generated_artifacts()

if errors:
    print("LINK / RELEASE-INTEGRITY VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("LINK / RELEASE-INTEGRITY VALIDATION PASSED")
