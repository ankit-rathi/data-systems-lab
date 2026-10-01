# DATA-1063 — Data quality

**Level:** L2  
**Primary notebook:** 12 — Data Quality  
**Business symptom:** Shipment feed contains impossible states

## Mission

Investigate invalid shipment states, decide which records can be quarantined, and add a publication gate without hiding the underlying data problem.

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
- **12 — 12_data_quality** → [`03_reliable_data_engineering/12_data_quality.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/12_data_quality.ipynb)
- **14 — 14_mini_analytical_platform** → [`03_reliable_data_engineering/14_mini_analytical_platform.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/14_mini_analytical_platform.ipynb)
- **15 — 15_data_contracts** → [`04_quality_observability_orchestration/15_data_contracts.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/15_data_contracts.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
