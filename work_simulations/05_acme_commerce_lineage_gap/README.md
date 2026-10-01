# DATA-1081 — Metadata and lineage

**Level:** L2  
**Primary notebook:** 16 — Metadata & Lineage  
**Business symptom:** Marketing cannot trace a KPI to its source

## Mission

Trace the metric through datasets and transformations, identify the missing lineage edge, and propose metadata that makes impact analysis possible.

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
- **16 — 16_metadata_lineage** → [`04_quality_observability_orchestration/16_metadata_lineage.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/16_metadata_lineage.ipynb)
- **17 — 17_orchestration_dags** → [`04_quality_observability_orchestration/17_orchestration_dags.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/17_orchestration_dags.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
