"""Run work-simulation tests in isolated subprocesses.

The runner deliberately uses one subprocess at a time. This is slower than
parallel execution but much more deterministic across Colab, CI and local
machines, while keeping every scenario isolated from the others.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = sorted(p for p in (ROOT / 'work_simulations').iterdir() if p.is_dir() and (p / 'tests').exists())
timeout_seconds = int(os.environ.get('SCENARIO_TIMEOUT_SECONDS', '15'))
failed: list[str] = []

print(f'Running {len(SCENARIOS)} isolated scenario suites (timeout={timeout_seconds}s).', flush=True)
for scenario in SCENARIOS:
    env = {k: v for k, v in os.environ.items() if k not in {'PYTHONPATH', 'PYTEST_ADDOPTS'}}
    env['PYTEST_DISABLE_PLUGIN_AUTOLOAD'] = '1'
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['PYTHONPATH'] = str(scenario.resolve())
    print(f'\n=== {scenario.name} ===', flush=True)
    try:
        proc = subprocess.run(
            [sys.executable, '-m', 'pytest', '-q', 'tests', '--disable-warnings', '-p', 'no:cacheprovider'],
            cwd=scenario,
            env=env,
            text=True,
            stdin=subprocess.DEVNULL,
            timeout=timeout_seconds,
        )
        if proc.returncode:
            failed.append(scenario.name)
    except subprocess.TimeoutExpired:
        print(f'TIMED OUT after {timeout_seconds}s', file=sys.stderr, flush=True)
        failed.append(scenario.name)

if failed:
    print('\nSCENARIO TESTS FAILED')
    print('\n'.join('- ' + x for x in failed))
    raise SystemExit(1)
print(f'\nSCENARIO TESTS PASSED: {len(SCENARIOS)} isolated suites')
