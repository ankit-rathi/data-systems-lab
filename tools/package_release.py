"""Create a clean release archive after running release checks."""
from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT.parent/'data-systems-lab-latest-release.zip'
SHA=ROOT.parent/'data-systems-lab-latest-release.sha256'
for name in ('.pytest_cache','__pycache__','.ipynb_checkpoints'):
    found=list(ROOT.rglob(name))
    if found:
        print(f'RELEASE PACKAGING FAILED: generated artifacts found: {found}')
        raise SystemExit(1)

if OUTPUT.exists(): OUTPUT.unlink()
with zipfile.ZipFile(OUTPUT,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for path in sorted(ROOT.rglob('*')):
        if path.is_file():
            rel=path.relative_to(ROOT.parent)
            z.write(path,rel.as_posix())

digest=hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
SHA.write_text(f'{digest}  {OUTPUT.name}\n',encoding='utf-8')
print(f'PACKAGE: {OUTPUT}')
print(f'SHA256: {digest}')
