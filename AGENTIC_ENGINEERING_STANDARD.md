# Agent-Native Engineering Standard

## Purpose

This lab teaches engineering in a world where AI agents increasingly perform implementation, testing, documentation and operational tasks. The durable human skill is not typing code faster; it is turning intent into safe systems and proving that those systems work.

## The learner loop

```text
Understand → Specify → Delegate → Inspect → Verify → Break → Diagnose
→ Decide → Operate → Defend
```

Manual implementation is still used when it exposes a first-principles mechanism. It is not treated as the default measure of engineering ability.

## Every agent-assisted exercise should make four things explicit

| Layer | Learner question |
|---|---|
| Agent can do | What implementation or analysis can be delegated? |
| Human must understand | What mechanism must the learner be able to explain? |
| Human must verify | What evidence can independently establish correctness? |
| Human must decide | What trade-off, authorization or production judgment remains? |

## Minimum evidence

An agent-native exercise should preserve:

1. **Intent** — requirement and constraints.
2. **Context** — schemas, policies, architecture and relevant evidence supplied to the agent.
3. **Delegation** — the task assigned to the agent.
4. **Output** — what the agent proposed or changed.
5. **Inspection** — what the learner noticed in the output.
6. **Verification** — tests, measurements, traces or independent checks.
7. **Failure** — at least one adversarial or boundary case.
8. **Decision** — ship, revise, reject or escalate, with evidence.

## What this standard does not mean

- It does not require a live commercial model.
- It does not teach one vendor's prompt syntax as a durable skill.
- It does not pretend deterministic fake agents have the same behavior as frontier models.
- It does not remove coding from the curriculum.

Offline agent simulations are deliberately deterministic. They teach control flow, verification and governance without requiring paid APIs or unpredictable external services.

## Human advantage

The course optimizes for skills that remain valuable as implementation becomes cheaper: requirements, semantic modeling, architecture, failure analysis, evaluation design, security, authorization, cost/latency trade-offs, production operations and defensible decisions.
