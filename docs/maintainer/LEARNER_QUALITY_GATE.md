# Learner Quality Gate

A notebook passes only when the learner can produce evidence of reasoning, not merely a successful final cell.

| Level | Required evidence | Typical location |
|---|---|---|
| L1 | Build, observe, controlled change | Foundations |
| L2 | Measurement, failure, diagnosis, improvement | Reliability / systems |
| L3 | Competing designs, quantitative trade-off, decision | Distributed / AI |
| L4 | Ambiguous requirements, architecture, failure, evidence, defense | Production / capstone |

Automated checks verify structure and artifact links. Human review should still inspect whether the experiment actually teaches the mechanism and whether the challenge is independently solvable.

## Agent-native quality gate

For agent-assisted work, passing requires an inspectable chain: **intent → context → delegation → output → independent verification → deliberate failure → decision → evidence**. A notebook does not pass merely because generated code runs. The learner must identify at least one thing the agent could plausibly get wrong and design evidence that would expose it.
