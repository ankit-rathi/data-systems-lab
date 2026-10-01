# 1152 — DATA-1152 — Online churn scores disagree with batch scores

**Level:** L2→L3
**Primary notebook:** 34 — Serving / freshness
**Business owner:** Acme Commerce Growth / ML Platform

## Customer report

Support sees different churn labels depending on which system they query. Trace feature definitions, freshness and transformation order across batch and serving paths.

## What is known

- The core path must work locally and deterministically.
- The ticket describes symptoms, not the diagnosis.
- You are expected to leave evidence another engineer can review.

## Constraints

- No paid cloud service is required.
- Keep the original business question intact.
- Do not hide a data-time assumption inside the model code.

## Acceptance

1. State the prediction-time boundary.
2. Show the evidence that supports your diagnosis.
3. Add at least one regression or guardrail test.
4. Explain the business consequence in plain language.
5. Record what you would monitor or review after release.

## Notebook bridge

**Prepare with these notebooks:**
- **34 — Model Serving & Freshness** → [`06_ml_engineering/34_model_serving_freshness.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_ml_engineering/34_model_serving_freshness.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
