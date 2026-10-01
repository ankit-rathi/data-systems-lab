# DATA-1346 — Contain, rollback and recover an AI incident

**Workstream:** Production Engineering  
**Role:** Incident Commander  
**Decision:** Containment → recovery

## Mission

A new AI release increased error rate and duplicate support actions. Some failures are visible in system metrics; others appear only as business-side effects. You are the incident commander, not the person who originally wrote the change.

Build a timeline, identify the blast radius, choose containment, test rollback, and verify both technical recovery and recovery of business-side effects.

## What makes this situation real

- The first alert is not necessarily the first causal event.
- Rollback can restore software while leaving data or business side effects behind.
- Incident evidence must be preserved before cleanup changes the scene.
- An AI release may fail in ways that conventional availability metrics do not capture.

## Definition of done

1. Build a timestamped incident timeline.
2. Separate observed facts from hypotheses.
3. Define blast radius and containment criteria.
4. Execute or simulate rollback with evidence.
5. Verify business-side-effect recovery separately from software recovery.
6. Produce follow-up actions with owners, evidence and regression tests.

## Agent-native operating mode

This scenario may be solved with an implementation or investigation agent. Treat the agent as a contributor, not the authority. Record the requirement and context you supplied, inspect the proposed change or diagnosis, design an independent verification, deliberately challenge one assumption, and record the human decision: **ship, revise, reject or escalate**. Do not expose credentials, private prompts or proprietary data in evidence.

## Notebook bridge

**Prepare with these notebooks:**
- **53 — Incident Response, Rollback & Recovery** → [`09_production_architecture_capstones/53_incident_response_rollback_recovery.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/09_production_architecture_capstones/53_incident_response_rollback_recovery.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
