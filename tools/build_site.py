"""Build the minimal editorial GitHub Pages front door for the lab."""
from pathlib import Path
import csv, html, shutil

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ASSETS = SITE / "assets"
SKETCH_SRC = ROOT / "assets" / "sketch-notes"
SKETCH_DST = ASSETS / "sketch-notes"
SITE.mkdir(exist_ok=True)
ASSETS.mkdir(exist_ok=True)

# Synchronize sketch-note assets without touching the parent site's CSS layer.
if SKETCH_DST.exists():
    shutil.rmtree(SKETCH_DST)
shutil.copytree(SKETCH_SRC, SKETCH_DST)

manifest = list(csv.DictReader((ROOT / "NOTEBOOK_MANIFEST.csv").open(newline="", encoding="utf-8")))
manifest = [r for r in manifest if r.get("path") and Path(r["path"]).suffix == ".ipynb"]
manifest.sort(key=lambda r: int(Path(r["path"]).name[:2]))
capability_rows = list(csv.DictReader((ROOT / "CAPABILITY_MAP.csv").open(newline="", encoding="utf-8"))) if (ROOT / "CAPABILITY_MAP.csv").exists() else []
capability_by_id = {r["capability_id"]: r for r in capability_rows}
scenario_manifest_rows = list(csv.DictReader((ROOT / "APPRENTICESHIP_SCENARIOS.csv").open(newline="", encoding="utf-8"))) if (ROOT / "APPRENTICESHIP_SCENARIOS.csv").exists() else []
scenario_manifest_by_id = {r["scenario_id"]: r for r in scenario_manifest_rows}

phase_map = {
    "Foundations": ("00–01", "Foundations"),
    "Data Fundamentals": ("02–04", "Data Fundamentals"),
    "SQL & Databases": ("05–10", "SQL & Database Systems"),
    "Reliable Data Engineering": ("11–14", "Reliable Data Engineering"),
    "Quality & Observability": ("15–18", "Quality & Orchestration"),
    "Storage & Distributed Systems": ("19–24", "Storage & Distributed Systems"),
    "Big Data, Streaming & Lakehouse": ("25–30", "Big Data, Streaming & Lakehouse"),
    "ML Engineering": ("31–36", "ML Engineering"),
    "LLM Engineering": ("37–42", "LLM Engineering"),
    "AI Data Systems": ("43–48", "AI Data Systems"),
    "Production Architecture & Capstones": ("49–54", "Production Architecture & Capstones"),
}

def colab(path: str) -> str:
    return f"https://colab.research.google.com/github/ankit-rathi/data-systems-lab/blob/main/{path}"

def github(path: str) -> str:
    return f"https://github.com/ankit-rathi/data-systems-lab/blob/main/{path}"

scenario_root = ROOT / "work_simulations"
scenario_dirs = {}
for d in sorted(scenario_root.iterdir()):
    if d.is_dir() and d.name[:2].isdigit():
        scenario_dirs[int(d.name[:2])] = d

rows = []
current_phase = None
for r in manifest:
    n = int(Path(r["path"]).name[:2])
    phase = r["phase"]
    if phase != current_phase:
        rng, label = phase_map.get(phase, (f"{n:02d}", phase))
        rows.append(
            f'<tr class="lab-phase-row"><td colspan="7">{html.escape(rng)} &nbsp;·&nbsp; {html.escape(label)}</td></tr>'
        )
        current_phase = phase
    title = html.escape(r["title"])
    level = html.escape(r["level"])
    path = r["path"]
    scenario_ids = [x.strip() for x in r.get("apprenticeship", "").split(",") if x.strip()]
    if scenario_ids == ["FOUNDATION"] or not scenario_ids:
        apprenticeship_cell = '<span class="lab-muted">Foundation</span>'
    else:
        # Resolve S01/S02/... to the real scenario directory instead of
        # assuming the human-readable directory is the scenario id.
        apprenticeship_links = []
        for scenario_id in scenario_ids:
            if scenario_id.startswith("S") and scenario_id[1:].isdigit():
                scenario_dir = scenario_dirs.get(int(scenario_id[1:]))
                if scenario_dir is None:
                    raise ValueError(f"Unknown apprenticeship scenario: {scenario_id}")
                href = f"https://github.com/ankit-rathi/data-systems-lab/tree/main/work_simulations/{scenario_dir.name}"
            else:
                href = github("work_simulations")
            apprenticeship_links.append(f'<a class="lab-scenario-chip" href="{href}" target="_blank" rel="noopener">{html.escape(scenario_id)}</a>')
        apprenticeship_cell = ' '.join(apprenticeship_links)
    rows.append(
        '<tr>'
        f'<td>{n:02d}</td>'
        f'<td><a href="{github(path)}" target="_blank" rel="noopener">{title}</a></td>'
        f'<td>{html.escape(capability_by_id.get(r.get("capability_id"), {}).get("capability", phase))}</td>'
        f'<td>{level}</td>'
        f'<td>{html.escape(r.get("workstream", ""))}</td>'
        f'<td>{apprenticeship_cell}</td>'
        f'<td class="lab-colab"><a href="{colab(path)}" target="_blank" rel="noopener"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a></td>'
        '</tr>'
    )

scenario_rows = []
map_rows = list(csv.DictReader((ROOT / "APPRENTICESHIP_NOTEBOOK_MAP.csv").open(newline="", encoding="utf-8")))
by_scenario = {}
for mr in map_rows:
    for sid in mr["apprenticeship_scenarios"].split(","):
        if sid.startswith("S"):
            by_scenario.setdefault(sid, []).append(mr["notebook"])
for sid in range(1, 34):
    d = scenario_dirs[sid]
    ticket_text = (d/'ticket.md').read_text(encoding='utf-8')
    readme_text = (d/'README.md').read_text(encoding='utf-8')
    first = next((x.lstrip('# ').strip() for x in readme_text.splitlines() if x.startswith('# ')), d.name)
    m = __import__('re').search(r'DATA-\d+', first)
    fallback = __import__('re').search(r'DATA-\d+', ticket_text) or __import__('re').search(r'\b\d{4}\b', first)
    ticket = m.group(0) if m else (fallback.group(0) if fallback else f'S{sid:02d}')
    if ticket.isdigit(): ticket = 'DATA-' + ticket
    problem = first.split('—',1)[-1].strip() if '—' in first else first.replace(ticket, '').strip(' —')
    sids = by_scenario.get(f'S{sid:02d}', [])
    sid_key=f'S{sid:02d}'
    meta=scenario_manifest_by_id.get(sid_key, {})
    scenario_rows.append((sid_key, ticket, problem, meta.get('workstream',''), meta.get('primary_role',''), ', '.join(sids)))

scenario_html = "".join(
    '<tr>'
    f'<td>{sid}</td><td><a href="https://github.com/ankit-rathi/data-systems-lab/blob/main/work_simulations/{scenario_dirs[int(sid[1:])].name}/README.md" target="_blank" rel="noopener">{html.escape(ticket)}</a></td>'
    f'<td>{html.escape(pairing)}</td><td>{html.escape(problem)}</td><td>{html.escape(role)}</td>'
    '</tr>' for sid, ticket, problem, workstream, role, pairing in scenario_rows
)

content = f'''---
title: Data & AI Engineering Lab
description: A Colab-first, first-principles Data & AI Engineering apprenticeship by Ankit Rathi.
layout: default
permalink: /
---

<section class="lab-intro" aria-labelledby="lab-title">
  <div class="eyebrow">DATA · AI · ENGINEERING LAB</div>
  <h1 id="lab-title">Learn systems.<br><em>Then work on them.</em></h1>
  <p class="lab-lead">A free, Colab-first apprenticeship for learning how Data & AI systems behave — then using that knowledge in realistic engineering work at Acme Commerce.</p>
  <div class="lab-actions">
    <a class="button" href="#start">Start here →</a>
    <a class="text-link" href="#curriculum">Curriculum →</a>
    <a class="text-link" href="#missions">Acme missions →</a>
    <a class="text-link" href="https://ankit-rathi.github.io/">← Back to Ankit Rathi</a>
  </div>
</section>

<section class="lab-section lab-start" id="start" aria-labelledby="start-title">
  <div class="lab-section-label">IN 30 SECONDS</div>
  <h2 id="start-title">One course. Three things to remember.</h2>
  <div class="lab-row-list">
    <div class="lab-row"><span class="lab-row-number">01</span><span class="lab-row-copy"><strong>55 notebooks</strong><small>Controlled experiments that teach system mechanisms from first principles.</small></span></div>
    <div class="lab-row"><span class="lab-row-number">02</span><span class="lab-row-copy"><strong>33 Acme missions</strong><small>Realistic work situations where you investigate symptoms and make engineering decisions.</small></span></div>
    <div class="lab-row"><span class="lab-row-number">03</span><span class="lab-row-copy"><strong>One evidence trail</strong><small>Measurements, failures, verification and decisions become your engineering portfolio.</small></span></div>
  </div>
  <p class="lab-copy"><strong>The workflow:</strong> Notebook → Break → Diagnose → Acme mission → Verify → Decide → Evidence.</p>
  <p class="lab-note">You do not need to understand the repository before starting. <a href="https://github.com/ankit-rathi/data-systems-lab/blob/main/LEARNER_GUIDE.md" target="_blank" rel="noopener">Read the Learner Guide</a> if you want the full navigation model.</p>
</section>

<section class="lab-section" id="routes" aria-labelledby="routes-title">
  <div class="lab-section-label">CHOOSE YOUR ROUTE</div>
  <h2 id="routes-title">Start where your current ability makes sense.</h2>
  <div class="lab-table-wrap"><table class="lab-table" aria-label="Learner routes"><thead><tr><th>You are…</th><th>Start</th><th>Then</th></tr></thead><tbody>
    <tr><td>New to Data Engineering</td><td><a href="{colab(manifest[0]['path'])}">00</a></td><td>Follow the curriculum in order</td></tr>
    <tr><td>Working Data Engineer</td><td>11–30</td><td>Use earlier notebooks for gaps; finish 49–54</td></tr>
    <tr><td>ML / AI Engineer</td><td>31–48</td><td>Use 00–30 for foundation gaps; finish 49–54</td></tr>
    <tr><td>Senior Engineer / Architect</td><td>49–54</td><td>Return to earlier labs when a decision exposes a gap</td></tr>
    <tr><td>Here mainly for hands-on work</td><td><a href="#missions">Acme missions</a></td><td>Use each mission's preparation notebooks</td></tr>
  </tbody></table></div>
</section>

<div class="lab-thinking" aria-label="Lab learning loop">Understand <span>→</span> Build <span>→</span> Break <span>→</span> Diagnose <span>→</span> Work <span>→</span> Verify <span>→</span> Decide <span>→</span> Defend</div>

<section class="lab-section" id="curriculum" aria-labelledby="curriculum-title">
  <div class="lab-section-label">CURRICULUM</div>
  <h2 id="curriculum-title">55 notebooks. One production arc.</h2>
  <p class="lab-copy">The notebook is the laboratory. The linked Acme mission is the work test. Open Colab when you are ready to build.</p>
  <div class="lab-table-wrap"><table class="lab-table" aria-label="Data and AI Engineering Lab curriculum"><thead><tr><th>#</th><th>Notebook</th><th>Capability</th><th>Level</th><th>Workstream</th><th>Acme</th><th>Colab</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
  <p class="lab-note">Need the complete notebook ↔ mission lookup? Use the <a href="https://github.com/ankit-rathi/data-systems-lab/blob/main/APPRENTICESHIP_MAP.md" target="_blank" rel="noopener">Apprenticeship Map</a>.</p>
</section>

<section class="lab-section" id="missions" aria-labelledby="missions-title">
  <div class="lab-section-label">ACME COMMERCE</div>
  <h2 id="missions-title">33 missions. Six workstreams. One evolving company.</h2>
  <p class="lab-copy">Do the preparation notebooks first. Then investigate the ticket without reopening the notebook as an answer key. Each mission names its preparation route.</p>
  <div class="lab-table-wrap"><table class="lab-table" aria-label="Acme Commerce apprenticeship missions"><thead><tr><th>Scenario</th><th>Ticket</th><th>Workstream</th><th>Mission</th><th>Role</th><th>Prepare</th></tr></thead><tbody>{scenario_html}</tbody></table></div>
</section>

<section class="lab-section" id="agent" aria-labelledby="agent-title">
  <div class="lab-section-label">AI AGENTS</div>
  <h2 id="agent-title">Use agents. Keep the judgment.</h2>
  <p class="lab-copy">When an agent helps, the learner specifies the task, controls permissions, inspects the result and verifies it independently. The repository includes a vendor-neutral Agent Workbench with bounded tools, traces, evaluations and adversarial cases.</p>
  <div class="lab-row-list">
    <a class="lab-row" href="https://github.com/ankit-rathi/data-systems-lab/tree/main/agent_lab" target="_blank" rel="noopener"><span class="lab-row-number">01</span><span class="lab-row-copy"><strong>Agent Workbench</strong><small>Practice bounded, inspectable agent work.</small></span><span class="lab-row-arrow">↗</span></a>
    <a class="lab-row" href="https://github.com/ankit-rathi/data-systems-lab/blob/main/AGENTIC_ENGINEERING_STANDARD.md" target="_blank" rel="noopener"><span class="lab-row-number">02</span><span class="lab-row-copy"><strong>Agent-Native Standard</strong><small>Specify → Delegate → Inspect → Verify.</small></span><span class="lab-row-arrow">↗</span></a>
  </div>
</section>

<section class="lab-section" id="evidence" aria-labelledby="evidence-title">
  <div class="lab-section-label">EVIDENCE</div>
  <h2 id="evidence-title">Finish with proof, not completion counts.</h2>
  <p class="lab-copy">Keep predictions, measurements, failures, diagnoses, tests, decisions and — when relevant — agent traces. The <a href="https://github.com/ankit-rathi/data-systems-lab/blob/main/EVIDENCE_PORTFOLIO.md" target="_blank" rel="noopener">Evidence Portfolio</a> and <a href="https://github.com/ankit-rathi/data-systems-lab/tree/main/portfolio_template" target="_blank" rel="noopener">portfolio template</a> give you a simple structure.</p>
</section>
'''


(SITE / "index.md").write_text(content, encoding="utf-8")
print(f"Generated site/index.md with {len(manifest)} notebooks and {len(scenario_rows)} apprenticeship milestones.")
