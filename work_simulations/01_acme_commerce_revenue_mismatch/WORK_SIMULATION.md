# Work Simulation 01 — Revenue Mismatch

**Level:** L2 — Engineering work  
**Company:** Acme Commerce  
**Primary connection:** Notebook 06 — SQL Joins & Aggregations  
**Secondary connections:** data grain, data quality, testing, incident diagnosis

## Learning objective

Recognize that a technically valid SQL query can still be wrong when the join grain does not match the business question.

## Scenario

Finance reports that yesterday's revenue number is materially higher than the payment gateway settlement report.

The learner is **not told the root cause**. Several explanations are plausible.

## Required work

1. Read the ticket and inspect the repository.
2. Establish the correct business grain for revenue.
3. Run the supplied query and observe the mismatch.
4. Form at least two hypotheses.
5. Prove the root cause with row-count / amount evidence.
6. Implement the smallest safe correction.
7. Add a regression test.
8. Record evidence in `evidence.md`.
9. Explain the result in technical and business language.

## Acceptance

The corrected revenue result must equal the settled payment amount for the supplied fixture and the regression test must pass.

## Simulation boundary

This is a deterministic teaching incident. It is intentionally small and does not model a real payment gateway, financial ledger or production security boundary.
