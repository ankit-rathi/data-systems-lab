# DATA-1273 — Human-In-The-Loop Workflows

## From: Acme Commerce Data & AI Platform

### Business request
Reviewers can approve or reject an AI decision, but a later audit cannot always reconstruct what they saw.

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
Trace one decision end to end, identify mutable evidence, and define the minimum immutable review record.

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
- **46 — Human-in-the-Loop Workflows** → [`08_ai_data_systems/46_human-in-the-loop-workflows.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/08_ai_data_systems/46_human-in-the-loop-workflows.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
