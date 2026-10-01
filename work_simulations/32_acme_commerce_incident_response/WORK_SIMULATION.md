# Work Simulation Standard — Incident Response, Rollback & Recovery

## Level
L3 → Production Architecture / Operations

## Primary concept
signals, containment, rollback, recovery and incident evidence

## Learner evidence
Ticket notes, measurements, code change, regression test, architecture decision and operational reasoning.

## Deliberate failure
The release has a known-good predecessor, but the team has not verified that rollback also restores safe downstream side effects.

## Production bridge
Explain what changes with scale, concurrency, security, failure recovery, cost, latency, data volume and operational ownership.


## Agent-native operating mode

This scenario may be solved with an implementation or investigation agent. Treat the agent as a contributor, not the authority. Record the requirement and context you supplied, inspect the proposed change or diagnosis, design an independent verification, deliberately challenge one assumption, and record the human decision: **ship, revise, reject or escalate**. Do not expose credentials, private prompts or proprietary data in evidence.
