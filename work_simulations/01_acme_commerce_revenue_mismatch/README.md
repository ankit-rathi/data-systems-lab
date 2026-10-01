# Acme Commerce — Revenue Mismatch

You have joined the data engineering team at Acme Commerce.

Finance says yesterday's revenue dashboard is **18% higher** than the payment settlement report.

Your job is to investigate before changing anything.

## Start here

1. Read [`ticket.md`](ticket.md).
2. Inspect the data in `data/`.
3. Read the existing query in `src/revenue_report.sql`.
4. Run the tests.
5. Investigate the mismatch.
6. Fix the implementation and add evidence to `evidence.md`.

Do not assume the ticket tells you which SQL concept is involved.


## Your task

1. **Understand the situation:** read the ticket and inspect the evidence.
2. **Find the cause:** write at least two hypotheses and test them.
3. **Make the smallest safe change:** preserve the business constraint and add a regression check.
4. **Prove it:** record before/after evidence and the production decision.

**Do not start by guessing the fix.** The ticket gives you the situation, not the diagnosis.
## Constraints

- Do not delete records to make the numbers match.
- Do not hard-code the expected answer.
- Preserve the business meaning of settled revenue.
- Keep the fix understandable.

## Evidence expected

Your completed work should show:

- what the correct grain is;
- what evidence proves the mismatch;
- which hypothesis was confirmed;
- the code change;
- regression tests;
- the before/after result;
- a short technical explanation;
- a short business explanation.

## Git suggestion

Treat this like a real change:

```text
issue → branch → investigate → fix → test → commit → PR → review
```

## Notebook bridge

**Prepare with these notebooks:**
- **05 — SQL Fundamentals** → [`02_sql_databases/05_sql_fundamentals.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/02_sql_databases/05_sql_fundamentals.ipynb)
- **06 — SQL Joins and Aggregations** → [`02_sql_databases/06_sql_joins_aggregations.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/02_sql_databases/06_sql_joins_aggregations.ipynb)
- **07 — SQL Window Functions** → [`02_sql_databases/07_sql_window_functions.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/02_sql_databases/07_sql_window_functions.ipynb)

**Learner rule:** finish the preparation notebooks first, then solve this ticket without using their outputs as the diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.

---

**Check your work:** [Open the reference solution](../../solutions/scenarios/S01.md) — only after you have completed the mission and recorded your evidence.
