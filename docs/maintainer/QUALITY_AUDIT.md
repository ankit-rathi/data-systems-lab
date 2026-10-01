# Quality Audit — v1.4

## Scope

This audit treats the repository as four products at once:

1. a learner experience;
2. a systems laboratory;
3. an open-source repository;
4. a GitHub Pages front door.

## Current checks

- **Notebook structure:** every learner notebook has a purpose, learning guidance, sketch note and prediction; 15–54 additionally require measurement, break, diagnosis, production bridge, challenge and evidence language.
- **Runtime syntax:** notebook Python cells are parsed by the repository validator; the v1.4 depth labs 15–24 and 37–54 were executed sequentially in a shared Python namespace to catch cell-order failures.
- **Sketch notes:** exactly one notebook-specific SVG reference per learner notebook; no placeholder assets.
- **Manifest:** all 55 learner notebooks are represented exactly once.
- **Pages:** generated site contains all 55 notebook rows and current 49–54 phase.
- **Apprenticeship:** 33 scenarios have required documentation and isolated tests.
- **Graph integrity:** notebook → manifest → README → Pages → apprenticeship → evidence links are checked.

## What remains a human review gate

Automated checks cannot decide whether an experiment is pedagogically strong. Before a release, inspect representative notebooks at each depth level and verify:

- the learner must predict before observing;
- the failure is reproducible and meaningful;
- measurements distinguish competing explanations;
- the challenge can be completed without hidden solution steps;
- the production bridge clearly separates toy behavior from real-system behavior;
- the evidence artifact is useful to another engineer.

## Known boundary

The curriculum remains intentionally offline/deterministic. A toy consensus, Spark-like, retrieval or AI model simulation demonstrates a mental model; it does not certify production behavior of the corresponding technology. Later releases should add real engine observations where they improve the learning signal without making paid infrastructure a prerequisite.
