# DATA-1070

**Status:** Open  
**Owner:** Acme Commerce Data Platform  
**Priority:** P1 learning simulation  
**Level:** L2

## Reported symptom

GMV doubled after a rerun

## Request

Investigate the issue, identify the evidence that separates plausible explanations, implement a defensible change, and document how the team should prevent recurrence.

## Constraints

- Core path must run locally with deterministic fixtures.
- Do not assume the ticket names the root cause.
- Preserve useful raw evidence.
- Add regression coverage for the failure you prove.

## Notebook bridge

**Prepare with these notebooks:**
- **13 — 13_incremental_idempotent** → [`03_reliable_data_engineering/13_incremental_idempotent.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/13_incremental_idempotent.ipynb)
- **14 — 14_mini_analytical_platform** → [`03_reliable_data_engineering/14_mini_analytical_platform.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/14_mini_analytical_platform.ipynb)
- **17 — 17_orchestration_dags** → [`04_quality_observability_orchestration/17_orchestration_dags.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/17_orchestration_dags.ipynb)
- **18 — 18_retries_backfills** → [`04_quality_observability_orchestration/18_retries_backfills.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/18_retries_backfills.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
