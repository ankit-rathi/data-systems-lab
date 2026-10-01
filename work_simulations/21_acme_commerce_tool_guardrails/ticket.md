# 1232 — AI assistant wants to take actions without clear authorization

**Level:** L2/L3
**Primary notebook:** 42 — Tool calling / agent loops
**Business owner:** Acme Commerce Support / AI Platform

## Customer report

The support assistant can look up orders and refunds. Product asks for automatic actions next. Before enabling writes, define tool allow-lists, argument validation and human escalation.

## What is known

- The core path must work locally and deterministically.
- The ticket describes symptoms, not the diagnosis.
- You are expected to leave evidence another engineer can review.

## Constraints

- No paid cloud service is required.
- Keep the business question intact.
- Do not hide a reliability or safety assumption inside application code.

## Acceptance

1. State the boundary or failure mode you investigated.
2. Show evidence that supports the diagnosis.
3. Add at least one regression or guardrail test.
4. Explain the business consequence in plain language.
5. Record the production follow-up.

## Notebook bridge

**Prepare with these notebooks:**
- **42 — Tool Calling & Agent Loops** → [`07_llm_engineering/42_tool_calling_agent_loops.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/07_llm_engineering/42_tool_calling_agent_loops.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
