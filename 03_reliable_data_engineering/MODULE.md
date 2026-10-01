# Module 03 — Reliable Data Engineering

**Purpose:** Turn isolated data-system mechanisms into a small, trustworthy, replayable analytical pipeline.

**Prerequisites:** 03–10, especially Parquet/columnar storage, SQL, transactions and data modeling.

**Learner outcome:** Trace data from ingestion to analytical product, enforce quality gates, make reruns safe, handle late data, and reason about operational state.

| # | Notebook | What you'll learn | Level | Status |
|---:|---|---|---|---|
| 11 | [API → Parquet → DuckDB](11_api_parquet_duckdb.ipynb) | Source contracts, raw/curated boundaries, Parquet publication and analytical querying | L1/L2 | Complete |
| 12 | [Data Quality](12_data_quality.ipynb) | Executable quality checks and publication decisions | L2 | Complete |
| 13 | [Incremental & Idempotent Pipelines](13_incremental_idempotent.ipynb) | Watermarks, stable keys, retries, late data and recovery | L2/L3 | Complete |
| 14 | [Mini Analytical Platform](14_mini_analytical_platform.ipynb) | End-to-end integration, data products and run observability | L2/L3 | Complete |

## Module arc

```text
Source → Raw → Validate → Curate → Query → Observe → Recover → Design
```
