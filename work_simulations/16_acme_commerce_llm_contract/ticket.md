# 1181 — LLM response latency is unpredictable

**Level:** L2/L3
**Primary notebook:** 37 — Model API contract / reliability
**Business owner:** Acme Commerce Support / AI Platform

## Customer report

Support has added an AI summarizer, but the request boundary does not record token counts or latency. Establish a measurable model-call contract before optimizing prompts.

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
- **37 — LLM Systems Foundations** → [`07_llm_engineering/37_llm_systems_foundations.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/07_llm_engineering/37_llm_systems_foundations.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
