# 1201 — Policy search misses paraphrased customer questions

## Your task

1. **Understand the situation:** read the ticket and inspect the evidence.
2. **Find the cause:** write at least two hypotheses and test them.
3. **Make the smallest safe change:** preserve the business constraint and add a regression check.
4. **Prove it:** record before/after evidence and the production decision.

**Do not start by guessing the fix.** The ticket gives you the situation, not the diagnosis.

This is the Acme Commerce apprenticeship scenario paired with **Notebook 39**.

## Work like an engineer

**Ticket → investigate → hypotheses → change → test → evidence → explain → operate**

Start with `ticket.md`. Do not look for the answer in the notebook. The notebook teaches the mechanism; this scenario asks you to discover where that mechanism matters.

## Required artifacts

- `ticket.md` — business request
- `data/` — deterministic fixture
- `src/` — learner implementation / inspection point
- `tests/` — acceptance check
- `evidence.md` — investigation record

## Notebook bridge

**Prepare with these notebooks:**
- **39 — Embeddings & Similarity** → [`07_llm_engineering/39_embeddings_similarity.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/07_llm_engineering/39_embeddings_similarity.ipynb)

**Learner rule:** finish the preparation notebooks first, then solve this ticket without using their outputs as the diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.

---

**Check your work:** [Open the reference solution](../../solutions/scenarios/S18.md) — only after you have completed the mission and recorded your evidence.
