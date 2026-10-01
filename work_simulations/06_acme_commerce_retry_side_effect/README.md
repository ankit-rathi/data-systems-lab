# DATA-1094 — Retries and backfills

**Level:** L2→L3  
**Primary notebook:** 18 — Retries, Backfills & Operational Semantics  
**Business symptom:** A retry created a duplicate downstream effect

## Mission

Separate retry safety from idempotency, reproduce the failure, and redesign the boundary so recovery does not multiply effects.

## Learner rule

Do not jump from the ticket to the fix. Inspect the evidence, write hypotheses, test them, then make the smallest defensible change.

## Required evidence

- ticket and business impact
- investigation notes and competing hypotheses
- code/query/config change
- tests or measured validation
- Git/PR-style summary
- production implication and prevention idea

This scenario is intentionally deterministic and educational. It is not a production payment, logistics, or security implementation.

## Notebook bridge

**Prepare with these notebooks:**
- **13 — 13_incremental_idempotent** → [`03_reliable_data_engineering/13_incremental_idempotent.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/13_incremental_idempotent.ipynb)
- **17 — 17_orchestration_dags** → [`04_quality_observability_orchestration/17_orchestration_dags.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/17_orchestration_dags.ipynb)
- **18 — 18_retries_backfills** → [`04_quality_observability_orchestration/18_retries_backfills.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/18_retries_backfills.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
