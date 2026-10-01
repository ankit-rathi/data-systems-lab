"""Cross-artifact graph validation for curriculum and apprenticeship integrity."""
from __future__ import annotations
import csv, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
errors=[]
manifest=list(csv.DictReader((ROOT/'NOTEBOOK_MANIFEST.csv').open(encoding='utf-8',newline='')))
manifest_paths={r['path'] for r in manifest}
notebooks={str(p.relative_to(ROOT)).replace('\\','/') for p in ROOT.rglob('*.ipynb') if '99_templates' not in p.parts}
if len(notebooks) != 55: errors.append(f'expected 55 learner notebooks, found {len(notebooks)}')
if notebooks-manifest_paths: errors += [f'manifest missing: {p}' for p in sorted(notebooks-manifest_paths)]
if manifest_paths-notebooks: errors += [f'manifest stale: {p}' for p in sorted(manifest_paths-notebooks)]

readme=(ROOT/'README.md').read_text(encoding='utf-8')
if '55 learner notebooks: 00–54' not in readme: errors.append('README does not state current 00–54 baseline')
if '00–48 completed' in readme or 'Next build' in readme: errors.append('README contains stale baseline language')

site=(ROOT/'site/index.md').read_text(encoding='utf-8') if (ROOT/'site/index.md').exists() else ''
for n in range(55):
    if f'<td>{n:02d}</td>' not in site: errors.append(f'Pages missing notebook {n:02d}')
for p in manifest_paths:
    if p not in site: errors.append(f'Pages missing manifest notebook path: {p}')
if site.count('<td>S') < 33: errors.append('Pages does not expose all 33 apprenticeship scenarios')
if 'APPRENTICESHIP_MAP.md' not in site: errors.append('Pages missing learner-facing cross-map link')

# Canonical machine-readable map.
map_path=ROOT/'APPRENTICESHIP_NOTEBOOK_MAP.csv'
if not map_path.exists():
    errors.append('missing APPRENTICESHIP_NOTEBOOK_MAP.csv')
    map_rows=[]
else:
    map_rows=list(csv.DictReader(map_path.open(encoding='utf-8',newline='')))
    if len(map_rows)!=55: errors.append(f'expected 55 notebook map rows, found {len(map_rows)}')
    map_nums={int(r['notebook']) for r in map_rows if r.get('notebook','').isdigit()}
    if map_nums != set(range(55)): errors.append('notebook map does not cover exactly 00–54')

scenario_dirs=sorted([p for p in (ROOT/'work_simulations').iterdir() if p.is_dir() and p.name[:2].isdigit()])
if len(scenario_dirs)!=33: errors.append(f'expected 33 scenarios, found {len(scenario_dirs)}')
scenario_ids={f'S{int(p.name[:2]):02d}' for p in scenario_dirs}
scenario_by_id={f'S{int(p.name[:2]):02d}': p for p in scenario_dirs}

scenario_manifest=ROOT/'APPRENTICESHIP_SCENARIOS.csv'
if not scenario_manifest.exists():
    errors.append('missing APPRENTICESHIP_SCENARIOS.csv')
else:
    scenario_rows=list(csv.DictReader(scenario_manifest.open(encoding='utf-8',newline='')))
    if len(scenario_rows)!=33: errors.append(f'expected 33 scenario manifest rows, found {len(scenario_rows)}')
    if {r['scenario_id'] for r in scenario_rows} != scenario_ids: errors.append('scenario manifest does not cover exactly S01–S33')
    for r in scenario_rows:
        if r['workstream'] not in {'Revenue Data Platform','Distributed Data Platform','ML Platform','AI Support Platform','Agentic Data Platform','Production Engineering'}:
            errors.append(f"unknown workstream for {r['scenario_id']}: {r['workstream']}")

# Every Sxx link exposed by the generated Pages source must contain the real
# scenario directory name, not merely the scenario id.
for sid, scenario_path in sorted(scenario_by_id.items()):
    expected=f'work_simulations/{scenario_path.name}'
    if expected not in site:
        errors.append(f'Pages missing actual scenario target for {sid}: {expected}')

# Validate the actual filesystem target for every mapped notebook → scenario edge.
for r in map_rows:
    for sid in [x.strip() for x in r.get('apprenticeship_scenarios','').split(',') if x.strip().startswith('S')]:
        if sid not in scenario_by_id:
            errors.append(f'{r["notebook"]} points to missing scenario directory: {sid}')
        else:
            scenario_path=scenario_by_id[sid]
            for required in ('README.md','ticket.md'):
                if not (scenario_path/required).exists():
                    errors.append(f'{sid} mapped target missing {required}')

map_text=(ROOT/'APPRENTICESHIP_MAP.md').read_text(encoding='utf-8')
if '55-notebook view' not in map_text or '33-scenario view' not in map_text: errors.append('apprenticeship map missing complete bidirectional views')
if 'Notebook → Scenario' not in map_text or 'Scenario → Notebook' not in map_text: errors.append('apprenticeship map missing routing explanation')

# Every scenario must be represented by at least one notebook and vice versa.
scenario_coverage=set()
for r in map_rows:
    for sid in [x.strip() for x in r.get('apprenticeship_scenarios','').split(',') if x.strip().startswith('S')]: scenario_coverage.add(sid)
for sid in sorted(scenario_ids):
    if sid not in scenario_coverage: errors.append(f'{sid} is not mapped to any notebook')
for r in map_rows:
    if r.get('apprenticeship_scenarios')=='FOUNDATION' and r['notebook'] not in {'00','01'}: errors.append(f'only 00–01 may be FOUNDATION: {r["notebook"]}')

# Learner-facing bridges in every notebook and scenario.
for r in map_rows:
    p=ROOT/r['notebook_path']
    if not p.exists(): continue
    data=json.loads(p.read_text(encoding='utf-8'))
    text='\n'.join(''.join(c.get('source',[])) for c in data.get('cells',[]) if c.get('cell_type')=='markdown')
    if '## Apprenticeship bridge' not in text: errors.append(f'{r["notebook"]} missing notebook apprenticeship bridge')
    if r['apprenticeship_scenarios']!='FOUNDATION':
        for sid in r['apprenticeship_scenarios'].split(','):
            if sid not in text: errors.append(f'{r["notebook"]} bridge missing {sid}')

for p in scenario_dirs:
    sid=f'S{int(p.name[:2]):02d}'
    for fn in ['README.md','ticket.md']:
        fp=p/fn
        if not fp.exists(): errors.append(f'{sid} missing {fn}'); continue
        text=fp.read_text(encoding='utf-8')
        if '## Notebook bridge' not in text: errors.append(f'{sid} {fn} missing notebook bridge')
    # At least one mapped notebook path must appear in README.
    mapped=[r['notebook'] for r in map_rows if sid in r.get('apprenticeship_scenarios','').split(',')]
    txt=(p/'README.md').read_text(encoding='utf-8') if (p/'README.md').exists() else ''
    if not mapped or not any(f'**{n}' in txt for n in mapped): errors.append(f'{sid} README does not expose mapped notebook(s)')

for required in ['README.md','NOTEBOOK_MANIFEST.csv','APPRENTICESHIP_MAP.md','APPRENTICESHIP_NOTEBOOK_MAP.csv','APPRENTICESHIP_SCENARIOS.csv','LEARNER_GUIDE.md','LEARNER_GUIDE.md','CHANGELOG.md','CONTEXT_HANDOFF.md','tools/build_site.py','tools/run_scenarios.py']:
    if not (ROOT/required).exists(): errors.append(f'missing graph root artifact: {required}')

if errors:
    print('GRAPH VALIDATION FAILED'); print('\n'.join('- '+e for e in errors)); sys.exit(1)
print(f'GRAPH VALIDATION PASSED: {len(notebooks)} notebooks, {len(scenario_dirs)} scenarios, {len(map_rows)} notebook mappings')
