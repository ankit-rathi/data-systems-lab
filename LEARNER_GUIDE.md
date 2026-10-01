# Learner Guide

This is the **one page to read after the README**. If you are unsure what to do next, come back here.

## 1. What are you actually doing?

You are learning how to **understand, build, break, verify and operate Data & AI systems** — then applying that knowledge to realistic engineering work at a fictional company called **Acme Commerce**.

There are three things to remember:

| Part | What it is | What you do |
|---|---|---|
| **Notebook** | A controlled engineering experiment | Learn a mechanism, predict, build, measure and break it |
| **Acme mission** | A realistic work situation | Investigate a symptom, form hypotheses, test them and decide |
| **Evidence** | Proof of your engineering judgment | Save measurements, failures, tests, decisions and artifacts |

You do **not** need to understand the whole repository before starting.

> **Simple rule:** learn a mechanism → practice it → work the mapped Acme mission → keep the evidence.

---

## 2. Where should I start?

Choose **one** route. Do not open every document or every scenario first.

| If you are… | Start here | Then |
|---|---|---|
| New to Data Engineering | Notebook **00** | Continue in order through the curriculum |
| A working Data Engineer | **11–30** | Use earlier notebooks only where a prerequisite is weak; finish with **49–54** |
| An ML / AI Engineer | **31–48** | Use **00–30** as foundation/gap checks; finish with **49–54** |
| A senior engineer / architect | **49–54** | Go back only when a production decision exposes a knowledge gap |
| Here mainly for hands-on work | **Acme missions** | Open the mission's **Prepare** notebooks first |

**Unsure? Start at 00.** You can change route later.

---

## 3. How one learning cycle works

Do this for each capability. The notebook tells you the mechanism; the mission asks you to use it without giving away the diagnosis.

```text
1. UNDERSTAND   Learn the mechanism and predict what should happen.
       ↓
2. BUILD        Run the experiment and inspect the result.
       ↓
3. BREAK        Change something deliberately and observe the failure.
       ↓
4. DIAGNOSE     Explain why the system behaved that way.
       ↓
5. WORK         Open the mapped Acme mission and investigate the symptom.
       ↓
6. VERIFY       Test your explanation and proposed change independently.
       ↓
7. DECIDE       Record the engineering or production decision.
       ↓
8. OPERATE      Consider recovery, monitoring, security and cost.
       ↓
9. DEFEND       Explain the evidence and trade-offs to another engineer.
```

When an AI agent is involved, add:

```text
SPECIFY → DELEGATE → INSPECT → VERIFY
```

The agent can help produce work. **You remain responsible for the requirement, permissions, verification and decision.**

---

## 4. How the 55 notebooks and 33 missions fit together

Think of the repository as **one curriculum with a work layer**, not two separate courses.

### The 12 capabilities

| Capability | Notebooks | Focus |
|---|---:|---|
| C01 | 00–04 | System foundations |
| C02 | 05–10 | Data access, querying and modeling |
| C03 | 11–15 | Correctness, contracts and idempotency |
| C04 | 16–18 | Lineage, orchestration and recovery |
| C05 | 19–24 | Storage, consistency and distributed systems |
| C06 | 25–30 | Streaming, lakehouse and scale |
| C07 | 31–36 | ML reliability |
| C08 | 37–42 | LLM systems |
| C09 | 43–48 | AI data systems |
| C10 | 49–50 | Agent-native engineering |
| C11 | 51–53 | Security, cost, incidents and recovery |
| C12 | 54 | Architecture defense |

### The six Acme workstreams

| Workstream | Missions | What you are learning to judge |
|---|---:|---|
| Revenue Data Platform | S01–S06 | Correctness, quality, lineage and recovery |
| Distributed Data Platform | S07–S09 | Latency, replication, streaming and scale |
| ML Platform | S10–S15 | Leakage, evaluation, serving, drift and rollback |
| AI Support Platform | S16–S21 | Structured output, retrieval, evaluation and tool boundaries |
| Agentic Data Platform | S22–S27 | AI-assisted operations, confidence, HITL and agent authority |
| Production Engineering | S28–S33 | Requirements, reliability, security, cost, incidents and architecture |

The scenarios deliberately become less scaffolded as you progress.

---

## 5. How do I find the right Acme mission?

You should **never have to guess**.

The website curriculum table shows the mapped **Acme** scenario for each notebook. Each scenario also tells you which notebooks prepare you for it.

For the complete bidirectional lookup, use:

**[Apprenticeship Map](APPRENTICESHIP_MAP.md)**

Use it when you want to answer either question:

- “I finished notebook 24 — which mission should I work next?”
- “I want to investigate S19 — which notebooks prepare me?”

The machine-readable maps (`APPRENTICESHIP_NOTEBOOK_MAP.csv` and `APPRENTICESHIP_SCENARIOS.csv`) are maintained for the repository tooling; learners normally do not need to open them.

---

## 6. What should I save?

Do not measure progress by notebook count alone. Keep a small evidence trail:

- **Prediction** — what did you expect?
- **Measurement** — what actually happened?
- **Failure** — what did you break?
- **Diagnosis** — what explains the failure?
- **Verification** — how did you prove the explanation/change?
- **Decision** — what would you ship, reject, roll back or monitor?
- **Agent evidence** — if an agent helped, what did you delegate and how did you verify it?

Use the **[Evidence Portfolio](EVIDENCE_PORTFOLIO.md)** when you want a structured place to keep this work. The ready-to-copy structure is in `portfolio_template/`.

---

## 7. How do I know I am getting better?

Use this simple mastery ladder:

```text
Explain → Reproduce → Experiment → Break → Transfer
                         ↓
             Operate → Delegate → Verify → Defend
```

The important transition is from **“I can make it run”** to **“I can establish whether it is correct and decide what should happen in production.”**

You do not need to reach every level in every notebook. Higher levels matter increasingly as you approach the later missions and Production Day.

---

## 8. How should I use AI agents?

Do not start by asking an agent to solve the whole lab.

A useful pattern is:

1. **Understand** the mechanism yourself.
2. **Specify** a bounded task with context and constraints.
3. **Delegate** only what you are prepared to inspect.
4. **Inspect** the generated work and assumptions.
5. **Verify** it independently with tests, measurements or a second method.
6. **Break** it with an adversarial or edge case.
7. **Decide** whether the result is acceptable.

The repository includes a vendor-neutral **Agent Workbench** for this practice. Start at [`agent_lab/README.md`](agent_lab/README.md) when you reach the AI-data/agent section.

For the detailed operating rules, see **[Agent-Native Engineering Standard](AGENTIC_ENGINEERING_STANDARD.md)**.

---

## 9. What not to do

- Do **not** read every Markdown file before starting.
- Do **not** jump between unrelated notebooks because the tools look interesting.
- Do **not** open an Acme mission before doing its preparation work unless you intentionally want an assessment challenge.
- Do **not** treat a passing notebook as proof that you understand the system.
- Do **not** let an agent become the source of truth for correctness.
- Do **not** optimize for completion counts.

The repository is deliberately designed so that the **website and README are the front door** and the deeper documents are reference material, not prerequisites.

---

## 10. The shortest mental model

If you remember only this, you have enough to start:

```text
                    DATA & AI ENGINEERING LAB
                              │
                 Learn a system mechanism
                              │
                         Run the lab
                              │
                     Break it on purpose
                              │
                     Understand the failure
                              │
                   Work the Acme mission
                              │
                    Verify your decision
                              │
                       Keep evidence
                              │
                     Defend the result
```

**Start:** [Notebook 00 — Environment & Colab](00_foundations/00_environment_colab.ipynb)

**Browse:** [GitHub Pages curriculum](site/index.md)

**Work:** [33 Acme missions](APPRENTICESHIP_MAP.md)

**Prove:** [Evidence Portfolio](EVIDENCE_PORTFOLIO.md)


## 7. What will I get from completing this?

If you actually do the experiments and missions — rather than just reading them — you finish with a practical engineering portfolio showing that you can:

- reason from **system mechanisms**, not tool names;
- diagnose failures from evidence instead of guessing;
- design data, ML, LLM and AI systems with explicit correctness boundaries;
- work safely with AI agents by specifying tasks, controlling permissions and verifying output;
- make production decisions involving reliability, security, cost, recovery and trade-offs;
- explain and defend your decisions to another engineer or architect.

The goal is not “55 notebooks completed.” The goal is **evidence that you can investigate, build, break, verify and defend real engineering decisions.**

## 8. How to use the solutions

Every learner notebook and Acme mission ends with a **Check your work** link. Use it only after your attempt.

**Recommended loop:**

`Attempt → Test → Write evidence → Check reference solution → Compare reasoning → Revise`

Reference solutions live in [`solutions/`](solutions/). They are separate from the learner path so the exercises remain spoiler-free. A different answer can still be correct when it is supported by evidence and respects the constraints.
