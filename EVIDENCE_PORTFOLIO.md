# Evidence Portfolio

The end product of the apprenticeship layer is not a completion count. It is a collection of verifiable engineering evidence.

## Evidence record

Each completed work simulation can contribute:

- ticket / issue
- investigation notes
- code change
- tests
- commit / PR
- review comments
- measurement
- incident or recovery note
- architecture decision, where applicable
- technical explanation
- business explanation

## Portfolio progression

```text
Ticket
  ↓
Diagnosis
  ↓
Implementation
  ↓
Tests
  ↓
Review
  ↓
Operational evidence
  ↓
Portfolio item
```

## Suggested portfolio summary

| Evidence | Target by end of apprenticeship |
|---|---:|
| Engineering tickets | 15+ |
| Failure investigations | 8+ |
| Production-style pipelines | 5+ |
| Architecture decisions | 3+ |
| Pull requests / reviews | 10+ |
| Performance investigations | 4+ |
| Incident reports | 4+ |
| AI/data applications | 2+ |
| End-to-end platform | 1 |

These are portfolio design targets, not grades or guarantees.

## Agent-native evidence

For AI-assisted work, preserve a lightweight record of requirement, context supplied, delegated task, material agent output, human review, verification evidence, failure discovered and final decision. Do not publish secrets, private prompts, credentials or proprietary data.

## Evidence provenance across the curriculum

For each apprenticeship artifact, record the notebook concepts that prepared you and the scenario where you applied them. A useful portfolio trace is:

```text
Notebook(s) → Scenario → Hypothesis → Evidence → Change → Verification → Decision
```

This makes the portfolio show not only *what* you built, but how learning transferred into ambiguous engineering work. Use [APPRENTICESHIP_MAP.md](APPRENTICESHIP_MAP.md) as the routing index.


## Reusable portfolio template

The repository includes [`portfolio_template/`](portfolio_template/) with a machine-readable `evidence_record.json` and nine evidence categories. Copy it into a personal portfolio rather than committing private learner evidence into the course repository.

Validate the template with `python tools/validate_portfolio.py`.
