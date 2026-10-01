# Data & AI Engineering Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ankit-rathi/data-systems-lab/blob/main/00_foundations/00_environment_colab.ipynb)

> **A free, Colab-first apprenticeship for learning how Data & AI systems actually behave — and how to engineer, verify and operate them in the age of AI agents.**

## In one minute

This is a **hands-on Data & AI engineering apprenticeship**. You learn a system mechanism, deliberately break it, diagnose what happened, then use the same idea in a realistic **Acme Commerce** engineering mission.

### What you get at the end

If you do the work — not just read it — you build evidence that you can:

- understand how data, ML, LLM, AI and distributed systems actually behave;
- diagnose failures from evidence rather than guess at fixes;
- design for correctness, reliability, security, cost and recovery;
- work safely with AI agents: **specify → delegate → inspect → verify**;
- defend architecture and production decisions like an engineer.

**Your output is not a pile of completed notebooks. It is an evidence-backed engineering portfolio.**

### The whole course in one line

`Notebook → Break → Diagnose → Acme mission → Verify → Decide → Evidence`

There are **55 learner notebooks (00–54)** and **33 Acme missions**, connected into one progression.

**Current notebook baseline: 55 learner notebooks: 00–54.** When a notebook or mission ends, its **Check your work** link takes you to a separate reference solution — after you have attempted it.

## Where should I start?

| You are… | Start with |
|---|---|
| New to Data Engineering | **[Notebook 00](00_foundations/00_environment_colab.ipynb)** |
| Already working in Data Engineering | **[Notebooks 11–30](site/index.md#curriculum)** |
| An ML / AI Engineer | **[Notebooks 31–48](site/index.md#curriculum)** |
| A senior engineer / architect | **[Notebooks 49–54](site/index.md#curriculum)** |
| Here for realistic engineering work | **[33 Acme missions](APPRENTICESHIP_MAP.md)** |

**Unsure? Start at 00.** You can change route later.

## The website is the front door

The **[GitHub Pages site](site/index.md)** gives you the shortest learner view:

- what the lab is;
- which route to take;
- the 55-notebook curriculum in one table;
- the six Acme workstreams;
- all 33 missions and their preparation notebooks;
- the Agent Workbench;
- how to build an evidence portfolio.

You should not need to understand the repository structure before beginning.

## What connects the pieces?

**Notebook** = controlled system experiment  
**Acme mission** = realistic work test  
**Evidence** = proof of your engineering judgment

The persistent company is **Acme Commerce**. Its 33 missions progress from data correctness and reliability through distributed systems, ML, LLMs, AI data systems, agentic operations and production architecture.

For the practical learner instructions, read the **[Learner Guide](LEARNER_GUIDE.md)**.

## Core learner references

- **[Learner Guide](LEARNER_GUIDE.md)** — how to navigate the course without getting lost.
- **[Apprenticeship Map](APPRENTICESHIP_MAP.md)** — notebook ↔ Acme mission lookup.
- **[Evidence Portfolio](EVIDENCE_PORTFOLIO.md)** — what proof to keep as you learn.
- **[Agent-Native Engineering Standard](AGENTIC_ENGINEERING_STANDARD.md)** — how to work safely with agents.

Everything else in the repository is implementation, scenario detail, templates, or maintainer material. **You do not need to read it first.**

## Curriculum at a glance

| Stage | Notebooks | Outcome |
|---|---:|---|
| Foundations | 00–04 | Python, representation and system mechanisms |
| Data & reliability | 05–18 | Querying, modeling, contracts, quality, lineage and recovery |
| Distributed systems | 19–30 | Storage, consistency, replication, streaming and scale |
| ML engineering | 31–36 | Framing, leakage, evaluation, serving, drift and rollback |
| LLM engineering | 37–42 | LLM systems, retrieval, evaluation and tools |
| AI data systems | 43–48 | AI contracts, quality, confidence, HITL and agent operations |
| Production architecture | 49–54 | Requirements, reliability, security, cost, incidents and defense |

**Full curriculum + Colab links:** [open the site](site/index.md#curriculum).

## Design principles

- Free and Colab-first; no paid cloud dependency for core learning.
- First principles before tools.
- Deterministic experiments where production services would add unnecessary friction.
- Simulations explicitly state what they prove and what they hide.
- The learner is evaluated on **evidence and judgment**, not notebook completion counts.
- The same vocabulary and workflow connect notebooks, Acme missions and production decisions.

## Maintainer / project information

- [Context Handoff](CONTEXT_HANDOFF.md) — current project state and architecture decisions.
- [Contributing](CONTRIBUTING.md) — repository contribution rules.
- [Changelog](CHANGELOG.md) — release history.
- Maintainer references live under [`docs/maintainer/`](docs/maintainer/).

## License

MIT.
