# Sketch Note Standard

Sketch notes are a first-class teaching artifact in the Data & AI Engineering Lab.

## Purpose

The sketch note answers one question before the learner reads code:

> **What should I picture in my head when I think about this system?**

It is not a decorative cover image and it is not a compressed copy of the notebook.

## Recommended composition

```text
┌──────────────────────────────────────────────┐
│ CONCEPT / SYSTEM                              │
│                                               │
│        [central mental model]                 │
│          ↙       ↓       ↘                    │
│       input   mechanism   output              │
│          ↘       ↓       ↙                    │
│           failure / trade-off                 │
│                                               │
│   “one sentence to remember”                  │
└──────────────────────────────────────────────┘
```

## Design rules

- One idea per sketch note.
- Prefer relationships, flows, boundaries and failure points over definitions.
- Use the same visual vocabulary across the curriculum where possible.
- Do not overcrowd the page with implementation details.
- Include the misconception the notebook is designed to correct when useful.
- For systems topics, show **where state lives** and **where failure can occur**.
- For performance topics, show the bottleneck and the measurement.
- For AI topics, show the evaluation/feedback loop, not only the model.

## Suggested recurring symbols

| Symbol | Meaning |
|---|---|
| cylinder | storage / database |
| rectangle | process / service |
| document | data artifact |
| arrow | data/control flow |
| clock | latency / time |
| scale icon | volume / growth |
| warning | failure / risk |
| loop | feedback / iteration |
| person | human-in-the-loop |

## Quality test

Hide the notebook text and look only at the sketch note.

A learner should be able to explain the basic mechanism in 30–60 seconds.


## Consistency rule

Notebook sketch notes use one visual language across the curriculum: warm paper background, handwritten typography, thick ink outlines, restrained pastel highlights, simple arrows/flows and a short production insight. The exact drawing can change with the concept, but the learner should recognize the family immediately.

For every new notebook: create the sketch note first, embed it in the notebook, copy it to the Pages site through the normal build, and validate the reference before the milestone is considered complete.
