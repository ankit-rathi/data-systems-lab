# DATA-1110 — Replication and consistency

## Mission

Treat this as a small engineering ticket, not a guided answer. Inspect the evidence, form at least two hypotheses, make the smallest defensible change, test it and record the result.

**Primary notebook:** 22 — Replication & Consistency
**System:** inventory reads
**Observed symptom:** regional reads disagree after a write
**Focus:** replica lag

## Learner path

1. Read `ticket.md` without opening the solution.
2. Inspect the data and current implementation.
3. Write two plausible hypotheses.
4. Run the existing tests or checks before changing code.
5. Implement the smallest fix.
6. Add or improve a regression test.
7. Record before/after evidence in `evidence.md`.
8. Write a short PR summary: problem, evidence, change, test, trade-off.

## Boundaries

The fixtures are deterministic teaching data. They model the failure mechanism, not a production gateway, database cluster or payment system. Do not infer production performance from the fixture.
