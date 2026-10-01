# DATA-1081

**Status:** Open  
**Owner:** Acme Commerce Data Platform  
**Priority:** P1 learning simulation  
**Level:** L2

## Reported symptom

Marketing cannot trace a KPI to its source

## Request

Investigate the issue, identify the evidence that separates plausible explanations, implement a defensible change, and document how the team should prevent recurrence.

## Constraints

- Core path must run locally with deterministic fixtures.
- Do not assume the ticket names the root cause.
- Preserve useful raw evidence.
- Add regression coverage for the failure you prove.

## Notebook bridge

**Prepare with these notebooks:**
- **16 — 16_metadata_lineage** → [`04_quality_observability_orchestration/16_metadata_lineage.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/16_metadata_lineage.ipynb)
- **17 — 17_orchestration_dags** → [`04_quality_observability_orchestration/17_orchestration_dags.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/17_orchestration_dags.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
