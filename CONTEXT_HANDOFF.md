# Context Handoff — v1.5.3 Phase 1

## Current state

`data-systems-lab` is a Colab-first, first-principles Data & AI Engineering apprenticeship with **55 learner notebooks (00–54)** and a parallel Acme Commerce work-simulation layer.

The current release is a **release-integrity pass**, following the v1.5 agent-native curriculum work. It fixes navigation integrity, mapping discoverability, test isolation and release hygiene before deeper course redesign phases. The main goal is to move the later curriculum from compact concept demonstrations toward small systems learners can operate, break, inspect and defend.

## Architecture

```text
notebook → manifest → README → GitHub Pages
        ↘ apprenticeship map → scenario → evidence
        ↘ standards / quality gates
```

The persistent company is Acme Commerce. Core learning remains free and deterministic; production services may be simulated when a real cloud dependency would distract from the concept. Every simulation must state its boundary.

## v1.4 changes

- 15–24: executable contracts, lineage, DAG scheduling, retry/backfill semantics, storage/recovery, MVCC, replication, partitioning and quorum experiments.
- 37–42: structured output, retrieval, evaluation, groundedness and agent authority depth.
- 43–48: AI data contracts, executable quality gates, confidence routing, auditable HITL, agentic data operations and evaluation learning loops.
- 49–54: measurable production requirements, SLO/error budgets, security boundaries, cost/capacity, incident recovery and capstone defense.
- README condensed; `CHANGELOG.md` is now the historical release record.
- Learning paths now map to explicit notebook ranges.
- Quality gates use L1–L4 experiment depth rather than a code-cell minimum.
- Site gets a compact Start Here router while retaining the parent site's minimal editorial visual language.

## v1.5.10 Phase 8 release-engineering changes

- Added `tools/smoke_notebooks.py` for structural notebook smoke and optional real execution.
- Added `tools/package_release.py` for clean release packaging and SHA-256.
- Added `.github/workflows/release.yml` for the explicit release gate and notebook execution smoke.
- The release gate now checks repository structure, content quality, graph, links, portfolio template and representative notebook structure.
- Local Jekyll execution remains environment-dependent; GitHub Pages CI is the authoritative renderer.

## v1.5.9 Phase 7 evidence-portfolio changes

- Added `portfolio_template/` with nine evidence categories and a reusable evidence record schema.
- Added `tools/validate_portfolio.py`; repository validation now checks the portfolio template structure.
- The website now links the portfolio template directly from the Evidence section.

## v1.5.8 Phase 6 web-experience changes

- GitHub Pages now leads with the capability model, Acme workstreams, apprenticeship missions, agent workbench and evidence rather than treating the notebook list as the primary information architecture.
- Curriculum is a scan-friendly table with capability, level, workstream, Acme mapping and Colab.
- The visual layer remains minimal/editorial and aligned to the parent site; sketch notes remain inside notebooks rather than decorating the landing page.

## v1.5.7 Phase 5 agent-workbench changes

- Added `agent_lab/` as a deterministic, vendor-neutral practical agent control plane.
- It contains the Agent Work Contract, permission ladder, tool gateway, traces, eval cases, prompt-injection attack, and deterministic grader.
- Notebooks 43–48 and scenarios S22–S27 now route learners into the Agent Workbench.
- Permission and human-approval enforcement happens outside the model proposal.

## v1.5.6 Phase 4 apprenticeship/workstream changes

- Added `LEARNER_GUIDE.md` and `APPRENTICESHIP_SCENARIOS.csv`.
- The 33 Acme scenarios are now explicitly grouped into six persistent workstreams with role and decision metadata.
- S28–S33 are now distinct production-review situations rather than generic variations: requirements, SLOs, security, cost/capacity, incident recovery, and production approval.

## v1.5.5 Phase 3 simulation-to-reality changes

- Added `LEARNER_GUIDE.md` and explicit reality-bridge sections to notebooks 25–30 and 37–42.
- Each bridge now states what the deterministic model proves, what real infrastructure hides, the relevant real-system technology/interface, and a transfer challenge.
- `NOTEBOOK_MANIFEST.csv` now includes `reality_bridge` metadata for these labs.

## v1.5.4 Phase 2 course-architecture changes

- The course is now explicitly modeled around capabilities rather than notebook count.
- Added `CAPABILITY_MAP.csv`, `LEARNER_GUIDE.md`, `LEARNER_GUIDE.md`, and `LEARNER_GUIDE.md`.
- `NOTEBOOK_MANIFEST.csv` now carries capability, workstream and primary-role metadata.
- All 55 learner notebooks contain a compact **Capability contract** with an explicit **You will prove** statement.
- The Acme layer is organized conceptually into six workstreams: Revenue Data Platform, Distributed Data Platform, ML Platform, AI Support Platform, Agentic Data Platform, and Production Engineering.

## v1.5.3 Phase 1 release-integrity changes

- Website curriculum scenario chips now resolve `S01`–`S33` through the actual `work_simulations/<directory>` names.
- Added `APPRENTICESHIP_MAP.md` as a human-readable learner-facing map; the CSV remains the machine-readable source.
- Corrected duplicated ticket labels in notebook apprenticeship bridges.
- Added `tools/validate_links.py` to validate Markdown/notebook/site links, GitHub and Colab targets, apprenticeship targets and release artifacts.
- Strengthened `tools/validate_graph.py` to verify actual scenario directories and generated Pages targets.
- Added `tools/release_check.py` for structural/site release validation.
- `tools/run_scenarios.py` now uses isolated, cache-free pytest subprocesses, configurable timeout and bounded concurrency.
- Added CI quality validation and release-cache hygiene.

## Source of truth

- Notebook metadata: `NOTEBOOK_MANIFEST.csv`
- Curriculum / front door: `README.md`
- Pages: generated by `python tools/build_site.py`
- Apprenticeship mapping: `APPRENTICESHIP_MAP.md`
- Standards: `LEARNER_GUIDE.md`, `docs/maintainer/SKETCH_NOTE_STANDARD.md`, `LEARNER_GUIDE.md`
- Current release history: `CHANGELOG.md`

## Validation

Run from repository root:

```bash
python tools/release_check.py
python tools/run_scenarios.py
```

Then manually open representative notebooks in a fresh Colab runtime and inspect the live GitHub Pages deployment.

## North star

Notebook 54 plus its paired Acme capstone is the culmination. Earlier modules should prepare learners to defend that final system: requirements, data contracts, reliability, security, cost, incident response, recovery and evidence.


## v1.5 agent-native direction

The curriculum is now intentionally designed for an agentic SDLC. Manual coding remains for first-principles learning, but professional evidence increasingly comes from requirements, context, delegation, inspection, independent verification, failure analysis, governance and production decisions. See AGENTIC_ENGINEERING_STANDARD.md and LEARNER_GUIDE.md.

## Apprenticeship mapping baseline

The current curriculum contains **55 learner notebooks (00–54) and 33 Acme Commerce apprenticeship scenarios**. Their relationship is now explicit and machine-validated in `APPRENTICESHIP_NOTEBOOK_MAP.csv` and documented in `APPRENTICESHIP_MAP.md`. Every notebook contains an apprenticeship bridge; every scenario names its preparation notebooks; the website exposes the same mapping.

When adding or changing a notebook/scenario, update the cross-map in the same milestone and run `python tools/release_check.py` followed by `python tools/run_scenarios.py`.


## v1.5.11 — Learner UX consolidation

The repository now has a deliberately simple learner front door. `README.md` gives the one-minute orientation; `LEARNER_GUIDE.md` is the single practical navigation guide; `APPRENTICESHIP_MAP.md`, `EVIDENCE_PORTFOLIO.md` and `AGENTIC_ENGINEERING_STANDARD.md` are the main deeper learner references. The GitHub Pages homepage mirrors the same mental model and no longer exposes a collection of competing architecture/role/standard documents.

Overlapping learner documents were consolidated into `LEARNER_GUIDE.md`. Maintainer-only documents were moved under `docs/maintainer/`. The redundant `APPRENTICESHIP_NOTEBOOK_MAP.md` was removed; the canonical learner cross-map is `APPRENTICESHIP_MAP.md`, while `APPRENTICESHIP_NOTEBOOK_MAP.csv` remains the machine-readable mapping used by validation and site generation.

No curriculum content was removed: the release still contains 55 learner notebooks (00–54), 33 Acme Commerce scenarios (S01–S33), the Agent Workbench, portfolio template, validation suite, scenario tests and release tooling.
