# DATA-1284 — Agentic Data Operations

**Level:** L2→L3
**Primary notebook:** 47 — Agentic Data Operations
**Business symptom:** an agent retries a data operation beyond its safe boundary

## Mission
Investigate the evidence, form at least two hypotheses, make the smallest defensible change, test it and document the operational trade-off.

## Required evidence
- business impact
- competing hypotheses
- evidence and diagnosis
- implementation change
- regression test
- before/after measurement where relevant
- technical and business explanation


## Agent-native operating mode

This scenario may be solved with an implementation or investigation agent. Treat the agent as a contributor, not the authority. Record the requirement and context you supplied, inspect the proposed change or diagnosis, design an independent verification, deliberately challenge one assumption, and record the human decision: **ship, revise, reject or escalate**. Do not expose credentials, private prompts or proprietary data in evidence.

## Agent Workbench

Use the vendor-neutral [`agent_lab/`](../../agent_lab/README.md) as the control plane for this ticket. Record the work contract, permission level, proposed action, independent verification, attack/challenge attempted, and human decision.

The agent may assist with implementation or investigation, but the learner remains accountable for requirements, permissions, evidence and acceptance.

## Notebook bridge

**Prepare with these notebooks:**
- **47 — Agentic Data Operations** → [`08_ai_data_systems/47_agentic-data-operations.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/08_ai_data_systems/47_agentic-data-operations.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
