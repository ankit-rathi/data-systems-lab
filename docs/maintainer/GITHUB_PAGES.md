# GitHub Pages

The Pages front door is intentionally minimal and editorial. It should feel like a focused extension of the parent site, not a dashboard.

## Current structure

- compact hero;
- **Start Here** routing by learner profile;
- Learn / Work / Prove model;
- apprenticeship table;
- curriculum table for notebooks 00–54;
- evidence links;
- visible back-to-parent-site link.

Sketch notes remain inside notebooks. They are not used as decorative landing-page cards.

## Source of truth

Run:

```bash
python tools/build_site.py
```

The builder reads `NOTEBOOK_MANIFEST.csv`, copies sketch-note assets, and generates `site/index.md`. Do not hand-edit the generated curriculum table.

## Acceptance

Before deployment:

1. run `python tools/quality_check.py`;
2. run `python tools/validate_graph.py`;
3. run `python tools/validate_repo.py`;
4. run `python tools/run_scenarios.py`;
5. open the generated site at desktop and mobile widths;
6. open representative Colab links from each phase;
7. verify the parent-site back link and curriculum table.
