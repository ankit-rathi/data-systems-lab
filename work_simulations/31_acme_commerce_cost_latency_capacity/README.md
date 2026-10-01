# DATA-1335 — Capacity and cost trade-off before scale-up

**Workstream:** Production Engineering  
**Role:** Platform Engineer  
**Decision:** Capacity → cost

## Mission

Traffic and AI workload volume are increasing. The team can add capacity, optimize the workload, or change the service policy. Finance wants a predictable cost envelope; engineering wants headroom for bursts.

Build a capacity model from the evidence, identify the dominant cost/latency drivers, and compare at least two mitigation strategies.


## Your task

1. **Understand the situation:** read the ticket and inspect the evidence.
2. **Find the cause:** write at least two hypotheses and test them.
3. **Make the smallest safe change:** preserve the business constraint and add a regression check.
4. **Prove it:** record before/after evidence and the production decision.

**Do not start by guessing the fix.** Your job is to explain the mechanism with evidence.
## What makes this situation real

- Average load can hide burst capacity requirements.
- Lower latency can increase cost; lower cost can increase queueing or failure risk.
- Capacity assumptions are uncertain and should be represented explicitly.
- Optimization without a measurement plan can simply move the bottleneck.

## Definition of done

1. Define workload units and forecast assumptions.
2. Calculate required capacity and headroom.
3. Separate fixed, variable and burst-related costs.
4. Compare at least two mitigation strategies.
5. Define the metric that would trigger another capacity review.
6. State the operational risk of under-provisioning and over-provisioning.

## Agent-native operating mode

This scenario may be solved with an implementation or investigation agent. Treat the agent as a contributor, not the authority. Record the requirement and context you supplied, inspect the proposed change or diagnosis, design an independent verification, deliberately challenge one assumption, and record the human decision: **ship, revise, reject or escalate**. Do not expose credentials, private prompts or proprietary data in evidence.

## Notebook bridge

**Prepare with these notebooks:**
- **52 — Cost, Latency & Capacity Planning** → [`09_production_architecture_capstones/52_cost_latency_capacity.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/09_production_architecture_capstones/52_cost_latency_capacity.ipynb)

**Learner rule:** finish the preparation notebooks first, then solve this ticket without using their outputs as the diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.

---

**Check your work:** [Open the reference solution](../../solutions/scenarios/S31.md) — only after you have completed the mission and recorded your evidence.
