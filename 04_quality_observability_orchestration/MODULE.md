# Module 04 — Quality, Observability & Orchestration

**Purpose:** Make data expectations, pipeline state, dependencies and recovery policies explicit.

| # | Notebook | Core experiment | Level |
|---:|---|---|---|
| 15 | Data Contracts | Executable field and value expectations | L1/L2 |
| 16 | Metadata & Lineage | Run metadata and downstream impact traversal | L1/L2 |
| 17 | Orchestration & DAGs | Topological order and cycle detection | L1/L2 |
| 18 | Retries, Backfills & Operational Semantics | Bounded retry policy and replay safety | L2/L3 |

## Module arc

```text
Contract → Observe → Schedule → Recover
```

The module extends notebooks 11–14. Its models are deterministic and tool-neutral; no scheduler service or paid cloud account is required.
