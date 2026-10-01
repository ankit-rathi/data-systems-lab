# DATA-1284 — Agentic Data Operations

## From: Acme Commerce Data & AI Platform

### Business request
An automated data operator has repeated an action after a timeout and the team cannot tell whether the first attempt completed.

### What is known
- A production symptom is observable in the supplied fixtures.
- The current evidence is incomplete.
- At least two plausible hypotheses should be considered before changing the system.
- The core path must remain deterministic and testable.

### Constraints
- No paid cloud service is required.
- Preserve useful existing behavior unless a change is justified.
- Do not hide uncertainty inside application code.
- Capture evidence before and after the change.

### Your investigation
Reproduce the uncertain-completion case, inspect authority and action boundaries, and propose a safe retry policy.

### Definition of done
1. Reproduce the symptom.
2. Record the measurements and evidence that support the diagnosis.
3. Make a bounded, reversible change.
4. Add at least one regression or guardrail test.
5. Explain the business consequence in plain language.
6. Record the production follow-up: metric, owner or control, and what would trigger another investigation.

> **Do not treat the ticket as the diagnosis.** The point of the exercise is to discover the mechanism from evidence.

## Notebook bridge

**Prepare with these notebooks:**
- **47 — Agentic Data Operations** → [`08_ai_data_systems/47_agentic-data-operations.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/08_ai_data_systems/47_agentic-data-operations.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
