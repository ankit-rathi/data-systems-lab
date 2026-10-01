# Changelog

## v1.5.12 — Learner instructions + reference solutions

- Rewrote notebook and Acme-mission instructions around a simple learner contract: **Goal → Do this → Save → Done when**.
- Added a final **Check your work** link to all 55 learner notebooks.
- Added a final **Check your work** link to all 33 Acme scenario READMEs.
- Added `solutions/` with 55 notebook reference solutions and 33 scenario reference solutions, deliberately separated from the learner path.
- Added validation that every notebook/scenario has a matching reference solution and learner-facing link.
- Added a prominent homepage **The payoff** section explaining the practical engineering capabilities learners should gain.
- Added the same outcome framing to `README.md` and `LEARNER_GUIDE.md`.
- Preserved the existing curriculum, Agent Workbench, portfolio, scenarios and release gates.


## v1.5.11 — Learner UX consolidation

- Reworked the learner front door around one simple journey: notebook → break → diagnose → Acme mission → verify → decide → evidence.
- Added `LEARNER_GUIDE.md` as the single practical navigation guide for routes, curriculum, missions, mastery and agent use.
- Simplified `README.md` to a one-minute orientation and clear starting routes.
- Simplified the GitHub Pages homepage to an at-a-glance learner snapshot, route table, curriculum, Acme missions, agent workbench and evidence.
- Consolidated overlapping learner architecture documents into `LEARNER_GUIDE.md`.
- Moved maintainer-only references under `docs/maintainer/` so they no longer compete with the learner entry points.
- Removed the redundant human-readable notebook-map Markdown file; `APPRENTICESHIP_MAP.md` remains the learner-facing cross-map and the CSV remains the machine-readable source.
- Preserved all 55 learner notebooks, 33 scenarios, agent workbench, portfolio, validation and release tooling.

## v1.5.10 — Phase 8 Release Engineering

- Added `tools/smoke_notebooks.py` for representative structural notebook smoke tests and optional Jupyter execution.
- Added `tools/package_release.py` for clean ZIP creation and SHA-256 generation with cache-artifact enforcement.
- Added a dedicated GitHub Actions release workflow with the repository gate and optional notebook execution smoke.
- Hardened scenario execution to use the active Python interpreter, isolated environments and no bytecode/cache generation.
- Final release validation now covers repository structure, content quality, curriculum graph, links, portfolio template and notebook smoke.

## v1.5.9 — Phase 7 Evidence Portfolio

- Added `portfolio_template/` with nine evidence categories and a machine-readable `evidence_record.json`.
- Added `tools/validate_portfolio.py` and integrated portfolio-template checks into repository validation.
- Updated the website evidence section to expose the portfolio template.
- Clarified that mastery is demonstrated through evidence and production defense rather than notebook completion counts.

## v1.5.8 — Phase 6 Web Experience

- Rebuilt the GitHub Pages information architecture around capabilities, six Acme workstreams, 33 missions, the Agent Workbench and evidence.
- Reworked the curriculum table to expose capability, level, workstream, apprenticeship mapping and Colab in one scan-friendly view.
- Added direct navigation to the capability map, mastery rubric, role paths and agent workbench.
- Preserved the minimal editorial visual language and kept sketch notes out of the landing page.
- Kept the bidirectional apprenticeship map visible so learners can route from notebook to scenario and back.

## v1.5.7 — Phase 5 Agent Workbench

- Added a vendor-neutral deterministic `agent_lab/` with work contracts, permission policy, bounded tool gateway, traces, evaluation cases, attacks and graders.
- Added practical Agent Workbench bridges to notebooks 43–48 and scenarios S22–S27.
- Added explicit permission/approval enforcement outside the model.
- Added a prompt-injection exercise that treats data as untrusted input.

## v1.5.6 — Phase 4 Acme Workstream Apprenticeship

- Added `LEARNER_GUIDE.md` and `APPRENTICESHIP_SCENARIOS.csv` to model the 33 tickets as one evolving Acme organization.
- Added workstream, role and decision-mode context to apprenticeship scenarios.
- Reworked S28–S33 into distinct production situations: architecture requirements, SLO/error budget, security boundary, capacity/cost, incident recovery, and final approval review.
- Strengthened graph validation to require the scenario manifest and six-workstream taxonomy.

## v1.5.5 — Phase 3 Simulation-to-Reality Depth

- Added `LEARNER_GUIDE.md` as the standard for clearly separating first-principles simulations from real systems.
- Added explicit reality bridges to notebooks 25–30 and 37–42, including production boundaries and transfer challenges.
- Extended `NOTEBOOK_MANIFEST.csv` with `reality_bridge` metadata.
- Updated the notebook standard so toy implementations cannot be mistaken for production technologies.

## v1.5.4 — Phase 2 Course Architecture

- Added capability-based course architecture and explicit proof standards.
- Added `CAPABILITY_MAP.csv`, `LEARNER_GUIDE.md`, `LEARNER_GUIDE.md`, and `LEARNER_GUIDE.md`.
- Extended `NOTEBOOK_MANIFEST.csv` with capability, workstream and role metadata.
- Added a learner-facing Capability contract to all 55 learner notebooks, including an explicit “You will prove” statement.
- Clarified the six Acme workstreams and the L0–L8 mastery ladder without changing the underlying notebook/scenario inventory.

## v1.5.3 — Phase 1 Release Integrity

- Fixed generated curriculum apprenticeship links to resolve `S01`–`S33` to their real scenario directories.
- Added learner-facing `APPRENTICESHIP_MAP.md` alongside the canonical CSV map.
- Corrected duplicate notebook bridge labels such as `DATA-1051: DATA-1051`.
- Added offline local-link, GitHub/Colab target, mapping-target and release-artifact validation in `tools/validate_links.py`.
- Strengthened apprenticeship graph validation to check actual scenario targets.
- Added `tools/release_check.py` for the repository/site integrity gate.
- Made scenario tests isolated, cache-free and configurable, with bounded parallel execution.
- Added release hygiene rules for pytest and generated notebook caches.
- Added a CI quality workflow covering repository validation, graph/link checks and scenario tests.

## v1.5.2 — Apprenticeship ↔ Notebook Cross-Mapping

- Added a machine-readable `APPRENTICESHIP_NOTEBOOK_MAP.csv`.
- Added a complete 55-notebook / 33-scenario two-way map.
- Added an Apprenticeship bridge to every learner notebook.
- Added notebook preparation links to every apprenticeship README and ticket.
- Updated learner docs and website generation so the relationship is visible from either direction.
- Extended graph validation to verify bidirectional mapping and learner-facing bridge coverage.


## v1.5 — Agent-Native Engineering

- Reframed the learning loop around Understand → Specify → Delegate → Inspect → Verify → Break → Diagnose → Decide → Operate → Defend.
- Added `AGENTIC_ENGINEERING_STANDARD.md` and `LEARNER_GUIDE.md`.
- Added human/agent responsibility guidance across notebook, learner, work-simulation and evidence standards.
- Added agent-native exercises to notebooks 43–48 and the production capstone 54.
- Updated the Pages build to represent all 55 notebooks and the agent-native production journey.
- Kept the course vendor-neutral, offline-first and deterministic where live model access is unnecessary.

v1.4 — Depth & Production Readiness

This release focuses on depth rather than adding another topic phase.

### Learning system
- Upgraded notebooks **15–24** into small systems laboratories with measurable experiments, deliberate failures and explicit diagnosis.
- Deepened **37–42** around structured-output validation, retrieval quality, groundedness, evaluation and agent authority.
- Reworked **43–48** into deterministic AI data-system workflows with contracts, quality proposals, confidence routing, auditability, agentic boundaries and learning loops.
- Reworked **49–54** into requirements, reliability, security, cost/capacity, recovery and architecture-defense exercises.
- Made **54** the north-star capstone: requirements → architecture evidence → incident → recovery → defense.

### Apprenticeship
- Tightened the later Acme scenarios so tickets lead with business symptoms and observable evidence rather than naming the diagnosis.
- Added stronger ambiguity, evidence requirements and operational follow-up expectations to the 22–33 lane.

### Documentation
- Rewrote README as a concise current front door; historical release detail moved here.
- Added explicit learning-path entry ranges.
- Clarified notebook, sketch-note, work-simulation and capstone standards.

### Maintainer tooling
- Added experiment-depth quality levels L1–L4.
- Added cross-artifact graph validation for notebook → manifest → README → Pages → apprenticeship → evidence.
- Added isolated subprocess execution for scenario tests.
- Regenerated GitHub Pages with a compact “Start here” router and 00–54 curriculum.

## v1.3

Production Architecture & Capstones 49–54, AI Data Systems 43–48, expanded apprenticeship and visual/documentation quality pass. See Git history for implementation detail.
