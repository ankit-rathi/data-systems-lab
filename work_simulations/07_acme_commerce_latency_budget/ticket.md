# DATA-1102

**Status:** Open  
**Owner:** Acme Commerce Data Platform  
**Priority:** P1 learning simulation  
**Level:** L2

## Reported symptom

Checkout query crossed the latency budget

## Request

Investigate the issue, identify the evidence that separates plausible explanations, implement a defensible change, and document how the team should prevent recurrence.

## Constraints

- Core path must run locally with deterministic fixtures.
- Do not assume the ticket names the root cause.
- Preserve useful raw evidence.
- Add regression coverage for the failure you prove.

## Notebook bridge

**Prepare with these notebooks:**
- **08 — Query Plans & Indexes** → [`02_sql_databases/08_query_plans_indexes.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/02_sql_databases/08_query_plans_indexes.ipynb)
- **09 — Transactions & Concurrency** → [`02_sql_databases/09_transactions_concurrency.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/02_sql_databases/09_transactions_concurrency.ipynb)
- **10 — Data Modeling** → [`02_sql_databases/10_data_modeling.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/02_sql_databases/10_data_modeling.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
