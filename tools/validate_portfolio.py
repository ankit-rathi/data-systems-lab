"""Validate the reusable learner portfolio template."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / 'portfolio_template'
errors=[]
required_dirs = [
    '01_requirements','02_architecture','03_data_contracts','04_experiments',
    '05_incidents','06_agent_work','07_decisions','08_evals','09_production_defense'
]
for d in required_dirs:
    if not (PORTFOLIO/d).is_dir(): errors.append(f'missing portfolio directory: {d}')
record=PORTFOLIO/'evidence_record.json'
if not record.exists():
    errors.append('missing portfolio/evidence_record.json')
else:
    try:
        data=json.loads(record.read_text(encoding='utf-8'))
        for key in ['id','source_notebooks','scenario','capability','mastery_target','problem','prediction_or_hypotheses','evidence','verification','decision','production_follow_up']:
            if key not in data: errors.append(f'evidence record missing field: {key}')
        if data.get('decision') not in {'ship|revise|reject|escalate','ship','revise','reject','escalate'}:
            errors.append('evidence record has invalid decision placeholder')
    except Exception as exc:
        errors.append(f'invalid evidence_record.json: {exc}')
if not (PORTFOLIO/'README.md').exists(): errors.append('missing portfolio README')
if errors:
    print('PORTFOLIO VALIDATION FAILED'); print('\n'.join('- '+x for x in errors)); sys.exit(1)
print('PORTFOLIO VALIDATION PASSED')
