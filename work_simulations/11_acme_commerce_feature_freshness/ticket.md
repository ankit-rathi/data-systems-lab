# 1138 — DATA-1138 — Churn score uses stale customer activity

**Level:** L2
**Primary notebook:** 32 — Features / leakage / freshness
**Business owner:** Acme Commerce Growth / ML Platform

## Customer report

Customer scores are generated every morning, but the feature table can be more than a day old. Determine which features are safe to use at scoring time and define a freshness gate.

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
- **32 — Features & Leakage** → [`06_ml_engineering/32_features_leakage.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_ml_engineering/32_features_leakage.ipynb)
- **34 — Model Serving & Freshness** → [`06_ml_engineering/34_model_serving_freshness.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_ml_engineering/34_model_serving_freshness.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
