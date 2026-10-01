# DATA-1302 — Architecture decision under competing requirements

**Workstream:** Production Engineering  
**Role:** Architecture Reviewer  
**Decision:** Requirements → architecture

## Mission

Checkout analytics and AI support are both growing, but they have different latency, freshness, reliability and data-access requirements. The platform team wants one architecture proposal before the next release.

Your job is not to draw a diagram first. Convert the business request into measurable requirements, identify incompatible assumptions, compare at least two architecture options, and record which evidence would change your decision.


## Your task

1. **Understand the situation:** read the ticket and inspect the evidence.
2. **Find the cause:** write at least two hypotheses and test them.
3. **Make the smallest safe change:** preserve the business constraint and add a regression check.
4. **Prove it:** record before/after evidence and the production decision.

**Do not start by guessing the fix.** Your job is to explain the mechanism with evidence.
## What makes this situation real

- Two workloads share data but have different operating characteristics.
- A technically elegant design can still violate an explicit business constraint.
- Some requirements are measurable; others are preferences that must be challenged.
- The fixture is deliberately incomplete. You must state what is unknown.

## Definition of done

1. Write the requirements and non-requirements separately.
2. Identify at least two plausible architectures.
3. Quantify the important workload/SLO assumptions.
4. Record rejected alternatives and why they were rejected.
5. Define the first production measurements that would validate the design.
6. State the conditions under which you would stop the rollout.

## Agent-native operating mode

This scenario may be solved with an implementation or investigation agent. Treat the agent as a contributor, not the authority. Record the requirement and context you supplied, inspect the proposed change or diagnosis, design an independent verification, deliberately challenge one assumption, and record the human decision: **ship, revise, reject or escalate**. Do not expose credentials, private prompts or proprietary data in evidence.

## Notebook bridge

**Prepare with these notebooks:**
- **49 — Production Architecture Requirements** → [`09_production_architecture_capstones/49_production_architecture_requirements.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/09_production_architecture_capstones/49_production_architecture_requirements.ipynb)

**Learner rule:** finish the preparation notebooks first, then solve this ticket without using their outputs as the diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.

---

**Check your work:** [Open the reference solution](../../solutions/scenarios/S28.md) — only after you have completed the mission and recorded your evidence.
