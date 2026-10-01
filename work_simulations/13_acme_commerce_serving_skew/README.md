# 1152 — DATA-1152 — Online churn scores disagree with batch scores

## Your task

1. **Understand the situation:** read the ticket and inspect the evidence.
2. **Find the cause:** write at least two hypotheses and test them.
3. **Make the smallest safe change:** preserve the business constraint and add a regression check.
4. **Prove it:** record before/after evidence and the production decision.

**Do not start by guessing the fix.** The ticket gives you the situation, not the diagnosis.

This is the Acme Commerce apprenticeship scenario paired with **Notebook 34**.

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
- **34 — Model Serving & Freshness** → [`06_ml_engineering/34_model_serving_freshness.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_ml_engineering/34_model_serving_freshness.ipynb)

**Learner rule:** finish the preparation notebooks first, then solve this ticket without using their outputs as the diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.

---

**Check your work:** [Open the reference solution](../../solutions/scenarios/S13.md) — only after you have completed the mission and recorded your evidence.
