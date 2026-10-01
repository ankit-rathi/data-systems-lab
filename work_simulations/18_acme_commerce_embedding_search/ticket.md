# 1201 — Policy search misses paraphrased customer questions

**Level:** L2/L3
**Primary notebook:** 39 — Embeddings / similarity
**Business owner:** Acme Commerce Support / AI Platform

## Customer report

Customers ask “money back” while the policy document says “refund”. The existing keyword search misses useful evidence. Investigate representation quality before changing the model.

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
- **39 — Embeddings & Similarity** → [`07_llm_engineering/39_embeddings_similarity.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/07_llm_engineering/39_embeddings_similarity.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
