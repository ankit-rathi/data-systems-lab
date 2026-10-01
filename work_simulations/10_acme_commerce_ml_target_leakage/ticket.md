# 1131 — DATA-1131 — Churn model looks excellent offline

**Level:** L2
**Primary notebook:** 31 — ML problem framing / leakage
**Business owner:** Acme Commerce Growth / ML Platform

## Customer report

Growth reports that the new churn model appears unusually accurate, but the team cannot explain which customer-time snapshot produced each feature. Investigate the target horizon and feature availability before trusting the metric.

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
- **31 — ML Problem Framing** → [`06_ml_engineering/31_ml_problem_framing.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_ml_engineering/31_ml_problem_framing.ipynb)
- **32 — Features & Leakage** → [`06_ml_engineering/32_features_leakage.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_ml_engineering/32_features_leakage.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
