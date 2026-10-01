# DATA-1324 — AI access boundary review

**Workstream:** Production Engineering  
**Role:** Security Reviewer  
**Decision:** Authorization boundary

## Mission

An AI workflow needs access to customer and payment-adjacent information to resolve support cases. The proposed workflow is useful, but its current tool/data boundary is wider than the business need.

Determine the minimum authority the workflow requires, which data should remain inaccessible, how identity and authorization should be enforced, and what evidence must be logged for every sensitive action.


## Your task

1. **Understand the situation:** read the ticket and inspect the evidence.
2. **Find the cause:** write at least two hypotheses and test them.
3. **Make the smallest safe change:** preserve the business constraint and add a regression check.
4. **Prove it:** record before/after evidence and the production decision.

**Do not start by guessing the fix.** Your job is to explain the mechanism with evidence.
## What makes this situation real

- The agent may be technically capable of requesting more data than it needs.
- User intent is not itself an authorization decision.
- Sensitive data can cross boundaries through tools, context and logs.
- A security control that cannot be audited is difficult to defend.

## Definition of done

1. Identify assets, actors, tools and trust boundaries.
2. Define least-privilege permissions for the workflow.
3. Separate read, write and irreversible actions.
4. Specify approval and audit requirements.
5. Add a misuse/negative test for an unauthorized request.
6. State the residual risk and escalation path.

## Agent-native operating mode

This scenario may be solved with an implementation or investigation agent. Treat the agent as a contributor, not the authority. Record the requirement and context you supplied, inspect the proposed change or diagnosis, design an independent verification, deliberately challenge one assumption, and record the human decision: **ship, revise, reject or escalate**. Do not expose credentials, private prompts or proprietary data in evidence.

## Notebook bridge

**Prepare with these notebooks:**
- **51 — Security, Governance & AI Boundaries** → [`09_production_architecture_capstones/51_security_governance_data_ai.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/09_production_architecture_capstones/51_security_governance_data_ai.ipynb)

**Learner rule:** finish the preparation notebooks first, then solve this ticket without using their outputs as the diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.

---

**Check your work:** [Open the reference solution](../../solutions/scenarios/S30.md) — only after you have completed the mission and recorded your evidence.
