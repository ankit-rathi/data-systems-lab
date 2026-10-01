# Ticket DATA-1042 — Revenue dashboard mismatch

## Reporter
Finance Analytics

## Priority
P1 — the daily revenue dashboard cannot currently be trusted.

## Business impact
Finance is preparing the daily settlement report and the dashboard does not agree with the payment gateway report.

## Symptoms
- Dashboard revenue is higher than settlement revenue.
- The mismatch appears in the supplied yesterday fixture.
- The current report query joins `orders` and `payments`.

## Plausible hypotheses
Investigate rather than assuming one is correct:

- duplicate orders;
- incorrect JOIN;
- cancelled transactions included;
- timezone boundary;
- payment timing / late-arriving data.

## Acceptance criteria

- Correct revenue is calculated at the business grain represented by settled payments.
- The supplied regression test passes.
- The implementation does not double-count a payment because a customer has multiple orders.
- Evidence explains why the original result was wrong.

## Notebook bridge

**Prepare with these notebooks:**
- **05 — SQL Fundamentals** → [`02_sql_databases/05_sql_fundamentals.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/02_sql_databases/05_sql_fundamentals.ipynb)
- **06 — SQL Joins and Aggregations** → [`02_sql_databases/06_sql_joins_aggregations.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/02_sql_databases/06_sql_joins_aggregations.ipynb)
- **07 — SQL Window Functions** → [`02_sql_databases/07_sql_window_functions.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/02_sql_databases/07_sql_window_functions.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
