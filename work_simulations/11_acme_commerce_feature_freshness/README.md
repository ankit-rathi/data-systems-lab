# 1138 — DATA-1138 — Churn score uses stale customer activity

This is the Acme Commerce apprenticeship scenario paired with **Notebook 32**.

## Work like an engineer

**Ticket → investigate → form hypotheses → change → test → evidence → explain → operate**

Start with `ticket.md`. Do not open the notebook first to look for the answer. The notebook teaches the mechanism; this scenario asks you to discover where that mechanism matters.

## Required artifacts

- `ticket.md` — business request
- `data/` — deterministic fixture
- `src/` — learner implementation
- `tests/` — acceptance / regression checks
- `evidence.md` — investigation record

This is a teaching simulation, not a real production ML system.

## Notebook bridge

**Prepare with these notebooks:**
- **32 — Features & Leakage** → [`06_ml_engineering/32_features_leakage.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_ml_engineering/32_features_leakage.ipynb)
- **34 — Model Serving & Freshness** → [`06_ml_engineering/34_model_serving_freshness.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_ml_engineering/34_model_serving_freshness.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
