"""Validate or execute a representative notebook smoke set.

Default mode is an offline structural smoke test. Use ``--execute`` when a
working Jupyter kernel environment is available (for example in CI/Colab).
Use ``--all --execute`` for a full local execution attempt.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DEFAULT=[
    '00_foundations/00_environment_colab.ipynb',
    '00_foundations/01_python_data_structures.ipynb',
    '01_data_fundamentals/02_files_json_apis.ipynb',
    '03_reliable_data_engineering/14_mini_analytical_platform.ipynb',
    '06_streaming_lakehouse/25_spark_execution_lazy.ipynb',
    '07_llm_engineering/37_llm_systems_foundations.ipynb',
    '08_ai_data_systems/43_ai-data-contracts.ipynb',
    '09_production_architecture_capstones/54_capstone_architecture_review.ipynb',
]

parser=argparse.ArgumentParser()
parser.add_argument('--all',action='store_true')
parser.add_argument('--execute',action='store_true')
parser.add_argument('--timeout',type=int,default=120)
args=parser.parse_args()

if args.execute:
    try:
        from nbclient import NotebookClient
    except ImportError:
        print('NOTEBOOK SMOKE FAILED: nbclient is not installed')
        raise SystemExit(1)

paths=sorted(ROOT.rglob('*.ipynb')) if args.all else [ROOT/p for p in DEFAULT]
failed=[]
for path in paths:
    print(f'=== {path.relative_to(ROOT)} ===',flush=True)
    try:
        nb=json.loads(path.read_text(encoding='utf-8'))
        if nb.get('nbformat',0)<4 or not nb.get('cells'):
            raise ValueError('invalid or empty notebook format')
        for i,cell in enumerate(nb.get('cells',[])):
            if cell.get('cell_type')!='code': continue
            source=''.join(cell.get('source',[]))
            try:
                ast.parse(source,filename=f'{path}:cell-{i}')
            except SyntaxError:
                if not any(line.lstrip().startswith(('%','!')) for line in source.splitlines()):
                    raise
        if args.execute:
            client=NotebookClient(
                nb,
                timeout=args.timeout,
                kernel_name='python3',
                resources={'metadata':{'path':str(path.parent)}},
            )
            client.execute()
        print('PASS',flush=True)
    except Exception as exc:
        failed.append((path,str(exc)))
        print(f'FAIL: {exc}',file=sys.stderr,flush=True)

if failed:
    print('\nNOTEBOOK SMOKE FAILED')
    for path,error in failed: print(f'- {path.relative_to(ROOT)}: {error}')
    raise SystemExit(1)
mode='execution' if args.execute else 'structural'
print(f'\nNOTEBOOK {mode.upper()} SMOKE PASSED: {len(paths)} notebooks')
