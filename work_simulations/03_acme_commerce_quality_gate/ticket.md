# DATA-1063

**Status:** Open  
**Owner:** Acme Commerce Data Platform  
**Priority:** P1 learning simulation  
**Level:** L2

## Reported symptom

Shipment feed contains impossible states

## Request

Investigate the issue, identify the evidence that separates plausible explanations, implement a defensible change, and document how the team should prevent recurrence.

## Constraints

- Core path must run locally with deterministic fixtures.
- Do not assume the ticket names the root cause.
- Preserve useful raw evidence.
- Add regression coverage for the failure you prove.

## Notebook bridge

**Prepare with these notebooks:**
- **12 — 12_data_quality** → [`03_reliable_data_engineering/12_data_quality.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/12_data_quality.ipynb)
- **14 — 14_mini_analytical_platform** → [`03_reliable_data_engineering/14_mini_analytical_platform.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/14_mini_analytical_platform.ipynb)
- **15 — 15_data_contracts** → [`04_quality_observability_orchestration/15_data_contracts.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/15_data_contracts.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
