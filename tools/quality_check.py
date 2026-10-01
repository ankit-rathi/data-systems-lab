"""Learner-oriented quality gate for the Data & AI Engineering Lab."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
issues=[]
notebooks=sorted(p for p in ROOT.rglob('*.ipynb') if '99_templates' not in p.parts and not any(x.startswith('.') for x in p.parts))

def text_of(d): return '\n'.join(''.join(c.get('source',[])) for c in d.get('cells',[]) if c.get('cell_type')=='markdown')
def has(text,*terms):
    low=text.lower(); return any(t.lower() in low for t in terms)

for p in notebooks:
    d=json.loads(p.read_text(encoding='utf-8')); text=text_of(d)
    if int(p.stem[:2])>=15:
        checks=[
          ('opening purpose',has(text,'why this exists','engineering problem')),
          ('learning outcome',has(text,'learning objectives','by the end','learning outcomes')),
          ('sketch note',has(text,'sketch note')),
          ('prediction',has(text,'predict before you run','prediction')),
          ('measurement',has(text,'## measure','measure behavior','measurement','observe / measure')),
          ('break',has(text,'break deliberately','break')),
          ('diagnosis',has(text,'## diagnose','diagnose','diagnosis')),
          ('production bridge',has(text,'production bridge','production implications','production')),
          ('independent challenge',has(text,'independent challenge','engineering challenge','challenge')),
          ('evidence',has(text,'evidence to keep','evidence')),
        ]
    else:
        checks=[('sketch note',has(text,'sketch note')),('prediction',has(text,'predict before you run','prediction'))]
    missing=[label for label,ok in checks if not ok]
    if missing: issues.append(f'{p.relative_to(ROOT)} missing: {", ".join(missing)}')
    if len(text.split())<150: issues.append(f'{p.relative_to(ROOT)} is too terse ({len(text.split())} markdown words)')
    code_cells=sum(c.get('cell_type')=='code' for c in d.get('cells',[]))
    if int(p.stem[:2])>=15 and code_cells<4: issues.append(f'{p.relative_to(ROOT)} has only {code_cells} code cells; depth pass expects at least 4')
    sketch_refs=re.findall(r'assets/sketch-notes/[^)\s]+\.svg',text)
    if len(sketch_refs)!=1: issues.append(f'{p.relative_to(ROOT)} has {len(sketch_refs)} sketch-note references; expected exactly 1')

scenarios=sorted(p for p in (ROOT/'work_simulations').iterdir() if p.is_dir() and not p.name.startswith('.'))
for s in scenarios:
    for f in ['README.md','ticket.md','evidence.md','WORK_SIMULATION.md']:
        if not (s/f).exists(): issues.append(f'{s.name} missing {f}')

# Later scenarios must ask for evidence rather than simply reveal a diagnosis.
for s in scenarios:
    try: t=(s/'ticket.md').read_text(encoding='utf-8').lower()
    except Exception: continue
    if int(re.match(r'(\d+)',s.name).group(1))>=22:
        for term in ['evidence','hypothes','regression','production']:
            if term not in t: issues.append(f'{s.name}/ticket.md missing learner-facing {term} requirement')

if issues:
    print('QUALITY CHECK FAILED'); print('\n'.join('- '+x for x in issues)); raise SystemExit(1)
print(f'Checked {len(notebooks)} learner notebooks and {len(scenarios)} apprenticeship scenarios.')
print('QUALITY CHECK PASSED')
