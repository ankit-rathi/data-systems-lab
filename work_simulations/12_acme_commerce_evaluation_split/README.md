# 1145 — DATA-1145 — Model review cannot reproduce the reported test score

This is the Acme Commerce apprenticeship scenario paired with **Notebook 33**.

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
- **33 — Train / Validation / Test** → [`06_ml_engineering/33_train_validation_test.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_ml_engineering/33_train_validation_test.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
