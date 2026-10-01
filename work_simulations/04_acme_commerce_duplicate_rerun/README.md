# DATA-1070 — Incremental and idempotent pipelines

**Level:** L2  
**Primary notebook:** 13 — Incremental & Idempotent Pipelines  
**Business symptom:** GMV doubled after a rerun

## Mission

Determine whether the rerun reprocessed valid records, design a stable-key/idempotency strategy, and prove that rerunning produces the same result.


## Your task

1. **Understand the situation:** read the ticket and inspect the evidence.
2. **Find the cause:** write at least two hypotheses and test them.
3. **Make the smallest safe change:** preserve the business constraint and add a regression check.
4. **Prove it:** record before/after evidence and the production decision.

**Do not start by guessing the fix.** Your job is to explain the mechanism with evidence.
## Learner rule

Do not jump from the ticket to the fix. Inspect the evidence, write hypotheses, test them, then make the smallest defensible change.

## Required evidence

- ticket and business impact
- investigation notes and competing hypotheses
- code/query/config change
- tests or measured validation
- Git/PR-style summary
- production implication and prevention idea

This scenario is intentionally deterministic and educational. It is not a production payment, logistics, or security implementation.

## Notebook bridge

**Prepare with these notebooks:**
- **13 — 13_incremental_idempotent** → [`03_reliable_data_engineering/13_incremental_idempotent.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/13_incremental_idempotent.ipynb)
- **14 — 14_mini_analytical_platform** → [`03_reliable_data_engineering/14_mini_analytical_platform.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/14_mini_analytical_platform.ipynb)
- **17 — 17_orchestration_dags** → [`04_quality_observability_orchestration/17_orchestration_dags.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/17_orchestration_dags.ipynb)
- **18 — 18_retries_backfills** → [`04_quality_observability_orchestration/18_retries_backfills.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/18_retries_backfills.ipynb)

**Learner rule:** finish the preparation notebooks first, then solve this ticket without using their outputs as the diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.

---

**Check your work:** [Open the reference solution](../../solutions/scenarios/S04.md) — only after you have completed the mission and recorded your evidence.
