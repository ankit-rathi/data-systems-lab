# 1190 — Support assistant outputs cannot be validated consistently

**Level:** L2/L3
**Primary notebook:** 38 — Structured output / validation
**Business owner:** Acme Commerce Support / AI Platform

## Customer report

The support assistant sometimes omits the action field. Downstream automation currently assumes every response is valid. Add an explicit validation boundary and preserve rejected responses for review.

## What is known

- The core path must work locally and deterministically.
- The ticket describes symptoms, not the diagnosis.
- You are expected to leave evidence another engineer can review.

## Constraints

- No paid cloud service is required.
- Keep the business question intact.
- Do not hide a reliability or safety assumption inside application code.

## Acceptance

1. State the boundary or failure mode you investigated.
2. Show evidence that supports the diagnosis.
3. Add at least one regression or guardrail test.
4. Explain the business consequence in plain language.
5. Record the production follow-up.

## Notebook bridge

**Prepare with these notebooks:**
- **38 — Structured Outputs & Validation** → [`07_llm_engineering/38_structured_outputs_validation.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/07_llm_engineering/38_structured_outputs_validation.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
