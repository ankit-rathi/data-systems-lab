# Apprenticeship ↔ Notebook Map

## How learners should use this map

The **33 Acme Commerce scenarios and 55 learner notebooks are one connected system**. A scenario is not a separate course. It is the workplace application of one or more notebook concepts.

**Notebook → Scenario:** finish the listed notebook experiment, then enter the linked ticket without using the notebook as an answer key.

**Scenario → Notebook:** start from the ticket when you want work first; the listed notebooks are the preparation/supporting concepts to review before or during investigation.

**Many-to-many is intentional:** real incidents cross system boundaries, so several notebooks can prepare one scenario and one notebook can support several scenarios.

## 55-notebook view

| # | Notebook | Apprenticeship scenario(s) | Role |
|---:|---|---|---|
| 00 | `Environment & Colab` | Foundation prerequisite for all scenarios | Foundation / cross-cutting |
| 01 | `Python Data Structures for Data Engineers` | Foundation prerequisite for all scenarios | Foundation / cross-cutting |
| 02 | `Files, JSON and APIs` | [S02 — Supplier API schema drift](work_simulations/02_acme_commerce_api_schema_drift/README.md) | Primary preparation / practice |
| 03 | `CSV vs JSON vs Parquet` | [S02 — Supplier API schema drift](work_simulations/02_acme_commerce_api_schema_drift/README.md) | Primary preparation / practice |
| 04 | `Apache Arrow and Columnar Memory` | [S02 — Supplier API schema drift](work_simulations/02_acme_commerce_api_schema_drift/README.md) | Primary preparation / practice |
| 05 | `SQL Fundamentals` | [S01 — Revenue dashboard mismatch](work_simulations/01_acme_commerce_revenue_mismatch/README.md) | Primary preparation / practice |
| 06 | `SQL Joins and Aggregations` | [S01 — Revenue dashboard mismatch](work_simulations/01_acme_commerce_revenue_mismatch/README.md) | Primary preparation / practice |
| 07 | `SQL Window Functions` | [S01 — Revenue dashboard mismatch](work_simulations/01_acme_commerce_revenue_mismatch/README.md) | Primary preparation / practice |
| 08 | `Query Plans & Indexes` | [S07 — Checkout query crossed the latency budget](work_simulations/07_acme_commerce_latency_budget/README.md) | Primary preparation / practice |
| 09 | `Transactions & Concurrency` | [S07 — Checkout query crossed the latency budget](work_simulations/07_acme_commerce_latency_budget/README.md) | Primary preparation / practice |
| 10 | `Data Modeling` | [S07 — Checkout query crossed the latency budget](work_simulations/07_acme_commerce_latency_budget/README.md) | Primary preparation / practice |
| 11 | `11_api_parquet_duckdb` | [S02 — Supplier API schema drift](work_simulations/02_acme_commerce_api_schema_drift/README.md) | Primary preparation / practice |
| 12 | `12_data_quality` | [S03 — Shipment quality gate](work_simulations/03_acme_commerce_quality_gate/README.md) | Primary preparation / practice |
| 13 | `13_incremental_idempotent` | [S04 — Duplicate rerun / GMV doubled](work_simulations/04_acme_commerce_duplicate_rerun/README.md), [S06 — Retry side effect](work_simulations/06_acme_commerce_retry_side_effect/README.md) | Primary preparation / practice |
| 14 | `14_mini_analytical_platform` | [S03 — Shipment quality gate](work_simulations/03_acme_commerce_quality_gate/README.md), [S04 — Duplicate rerun / GMV doubled](work_simulations/04_acme_commerce_duplicate_rerun/README.md) | Primary preparation / practice |
| 15 | `15_data_contracts` | [S02 — Supplier API schema drift](work_simulations/02_acme_commerce_api_schema_drift/README.md), [S03 — Shipment quality gate](work_simulations/03_acme_commerce_quality_gate/README.md) | Primary preparation / practice |
| 16 | `16_metadata_lineage` | [S05 — KPI lineage gap](work_simulations/05_acme_commerce_lineage_gap/README.md) | Primary preparation / practice |
| 17 | `17_orchestration_dags` | [S04 — Duplicate rerun / GMV doubled](work_simulations/04_acme_commerce_duplicate_rerun/README.md), [S05 — KPI lineage gap](work_simulations/05_acme_commerce_lineage_gap/README.md), [S06 — Retry side effect](work_simulations/06_acme_commerce_retry_side_effect/README.md) | Primary preparation / practice |
| 18 | `18_retries_backfills` | [S04 — Duplicate rerun / GMV doubled](work_simulations/04_acme_commerce_duplicate_rerun/README.md), [S06 — Retry side effect](work_simulations/06_acme_commerce_retry_side_effect/README.md) | Primary preparation / practice |
| 19 | `19_btree_lsm` | [S08 — Inventory reads disagree across regions](work_simulations/08_acme_commerce_replica_lag/README.md) | Primary preparation / practice |
| 20 | `20_wal_recovery` | [S08 — Inventory reads disagree across regions](work_simulations/08_acme_commerce_replica_lag/README.md) | Primary preparation / practice |
| 21 | `21_mvcc_isolation` | [S08 — Inventory reads disagree across regions](work_simulations/08_acme_commerce_replica_lag/README.md) | Primary preparation / practice |
| 22 | `22_replication_consistency` | [S08 — Inventory reads disagree across regions](work_simulations/08_acme_commerce_replica_lag/README.md) | Primary preparation / practice |
| 23 | `23_partitioning_hashing` | [S08 — Inventory reads disagree across regions](work_simulations/08_acme_commerce_replica_lag/README.md) | Primary preparation / practice |
| 24 | `24_raft_consensus` | [S08 — Inventory reads disagree across regions](work_simulations/08_acme_commerce_replica_lag/README.md) | Primary preparation / practice |
| 25 | `Spark Execution & Lazy Evaluation` | [S09 — Event stream backlog is growing](work_simulations/09_acme_commerce_stream_backlog/README.md) | Primary preparation / practice |
| 26 | `Shuffle, Partitioning & Skew` | [S09 — Event stream backlog is growing](work_simulations/09_acme_commerce_stream_backlog/README.md) | Primary preparation / practice |
| 27 | `Kafka Fundamentals & Partitioned Logs` | [S09 — Event stream backlog is growing](work_simulations/09_acme_commerce_stream_backlog/README.md) | Primary preparation / practice |
| 28 | `Event Time, Processing Time & Windows` | [S09 — Event stream backlog is growing](work_simulations/09_acme_commerce_stream_backlog/README.md) | Primary preparation / practice |
| 29 | `Delivery Semantics, Replay & Offsets` | [S09 — Event stream backlog is growing](work_simulations/09_acme_commerce_stream_backlog/README.md) | Primary preparation / practice |
| 30 | `Lakehouse Tables, Compaction & Schema Evolution` | [S09 — Event stream backlog is growing](work_simulations/09_acme_commerce_stream_backlog/README.md) | Primary preparation / practice |
| 31 | `ML Problem Framing` | [S10 — Churn model looks excellent offline](work_simulations/10_acme_commerce_ml_target_leakage/README.md) | Primary preparation / practice |
| 32 | `Features & Leakage` | [S10 — Churn model looks excellent offline](work_simulations/10_acme_commerce_ml_target_leakage/README.md), [S11 — Churn score uses stale customer activity](work_simulations/11_acme_commerce_feature_freshness/README.md) | Primary preparation / practice |
| 33 | `Train / Validation / Test` | [S12 — Model review cannot reproduce the reported test score](work_simulations/12_acme_commerce_evaluation_split/README.md) | Primary preparation / practice |
| 34 | `Model Serving & Freshness` | [S11 — Churn score uses stale customer activity](work_simulations/11_acme_commerce_feature_freshness/README.md), [S13 — Online churn scores disagree with batch scores](work_simulations/13_acme_commerce_serving_skew/README.md) | Primary preparation / practice |
| 35 | `Model Drift & Monitoring` | [S14 — Churn model performance is changing in production](work_simulations/14_acme_commerce_drift_monitoring/README.md) | Primary preparation / practice |
| 36 | `Rollback, Reproducibility & Model Registry` | [S15 — Candidate model degraded the support queue](work_simulations/15_acme_commerce_model_rollback/README.md) | Primary preparation / practice |
| 37 | `LLM Systems Foundations` | [S16 — LLM response latency is unpredictable](work_simulations/16_acme_commerce_llm_contract/README.md) | Primary preparation / practice |
| 38 | `Structured Outputs & Validation` | [S17 — Support assistant outputs cannot be validated consistently](work_simulations/17_acme_commerce_structured_support/README.md) | Primary preparation / practice |
| 39 | `Embeddings & Similarity` | [S18 — Policy search misses paraphrased questions](work_simulations/18_acme_commerce_embedding_search/README.md) | Primary preparation / practice |
| 40 | `Retrieval & RAG` | [S19 — Support answers cite the wrong policy](work_simulations/19_acme_commerce_rag_retrieval/README.md) | Primary preparation / practice |
| 41 | `LLM Evaluation & Groundedness` | [S20 — AI release review has no representative evaluation set](work_simulations/20_acme_commerce_llm_evaluation/README.md) | Primary preparation / practice |
| 42 | `Tool Calling & Agent Loops` | [S21 — AI assistant requests unauthorized actions](work_simulations/21_acme_commerce_tool_guardrails/README.md) | Primary preparation / practice |
| 43 | `AI Data Contracts` | [S22 — AI data contracts](work_simulations/22_acme_commerce_AI_data_contracts/README.md) | Primary preparation / practice |
| 44 | `AI-Assisted Data Quality` | [S23 — AI-assisted data quality](work_simulations/23_acme_commerce_AI-assisted_data_quality/README.md) | Primary preparation / practice |
| 45 | `Confidence & Escalation` | [S24 — Confidence and escalation](work_simulations/24_acme_commerce_confidence_and_escalation/README.md) | Primary preparation / practice |
| 46 | `Human-in-the-Loop Workflows` | [S25 — Human-in-the-loop workflow auditability](work_simulations/25_acme_commerce_human-in-the-loop_workflows/README.md) | Primary preparation / practice |
| 47 | `Agentic Data Operations` | [S26 — Agentic data operations](work_simulations/26_acme_commerce_agentic_data_operations/README.md) | Primary preparation / practice |
| 48 | `Learning Loops & AI Operations` | [S27 — Learning loops and AI operations](work_simulations/27_acme_commerce_learning_loops_and_AI_operations/README.md) | Primary preparation / practice |
| 49 | `Production Architecture Requirements` | [S28 — Production architecture requirements](work_simulations/28_acme_commerce_architecture_requirements/README.md) | Primary preparation / practice |
| 50 | `Reliability, SLOs & Failure Budgets` | [S29 — Reliability, SLOs and failure budgets](work_simulations/29_acme_commerce_reliability_slos/README.md) | Primary preparation / practice |
| 51 | `Security, Governance & AI Boundaries` | [S30 — Security, governance and AI boundaries](work_simulations/30_acme_commerce_security_governance/README.md) | Primary preparation / practice |
| 52 | `Cost, Latency & Capacity Planning` | [S31 — Cost, latency and capacity planning](work_simulations/31_acme_commerce_cost_latency_capacity/README.md) | Primary preparation / practice |
| 53 | `Incident Response, Rollback & Recovery` | [S32 — Incident response, rollback and recovery](work_simulations/32_acme_commerce_incident_response/README.md) | Primary preparation / practice |
| 54 | `Capstone Architecture Review` | [S33 — Capstone architecture review / Production Day](work_simulations/33_acme_commerce_capstone_architecture_review/README.md) | Primary preparation / practice |

## 33-scenario view

| Scenario | Ticket | Situation | Prepare with notebooks |
|---:|---|---|---|
| [S01](work_simulations/01_acme_commerce_revenue_mismatch/README.md) | DATA-1042 | Revenue dashboard mismatch | `05`, `06`, `07` |
| [S02](work_simulations/02_acme_commerce_api_schema_drift/README.md) | DATA-1051 | Supplier API schema drift | `02`, `03`, `04`, `11`, `15` |
| [S03](work_simulations/03_acme_commerce_quality_gate/README.md) | DATA-1063 | Shipment quality gate | `12`, `14`, `15` |
| [S04](work_simulations/04_acme_commerce_duplicate_rerun/README.md) | DATA-1070 | Duplicate rerun / GMV doubled | `13`, `14`, `17`, `18` |
| [S05](work_simulations/05_acme_commerce_lineage_gap/README.md) | DATA-1081 | KPI lineage gap | `16`, `17` |
| [S06](work_simulations/06_acme_commerce_retry_side_effect/README.md) | DATA-1094 | Retry side effect | `13`, `17`, `18` |
| [S07](work_simulations/07_acme_commerce_latency_budget/README.md) | DATA-1102 | Checkout query crossed the latency budget | `08`, `09`, `10` |
| [S08](work_simulations/08_acme_commerce_replica_lag/README.md) | DATA-1110 | Inventory reads disagree across regions | `19`, `20`, `21`, `22`, `23`, `24` |
| [S09](work_simulations/09_acme_commerce_stream_backlog/README.md) | DATA-1120 | Event stream backlog is growing | `25`, `26`, `27`, `28`, `29`, `30` |
| [S10](work_simulations/10_acme_commerce_ml_target_leakage/README.md) | DATA-1131 | Churn model looks excellent offline | `31`, `32` |
| [S11](work_simulations/11_acme_commerce_feature_freshness/README.md) | DATA-1138 | Churn score uses stale customer activity | `32`, `34` |
| [S12](work_simulations/12_acme_commerce_evaluation_split/README.md) | DATA-1145 | Model review cannot reproduce the reported test score | `33` |
| [S13](work_simulations/13_acme_commerce_serving_skew/README.md) | DATA-1152 | Online churn scores disagree with batch scores | `34` |
| [S14](work_simulations/14_acme_commerce_drift_monitoring/README.md) | DATA-1160 | Churn model performance is changing in production | `35` |
| [S15](work_simulations/15_acme_commerce_model_rollback/README.md) | DATA-1170 | Candidate model degraded the support queue | `36` |
| [S16](work_simulations/16_acme_commerce_llm_contract/README.md) | DATA-1181 | LLM response latency is unpredictable | `37` |
| [S17](work_simulations/17_acme_commerce_structured_support/README.md) | DATA-1190 | Support assistant outputs cannot be validated consistently | `38` |
| [S18](work_simulations/18_acme_commerce_embedding_search/README.md) | DATA-1201 | Policy search misses paraphrased questions | `39` |
| [S19](work_simulations/19_acme_commerce_rag_retrieval/README.md) | DATA-1210 | Support answers cite the wrong policy | `40` |
| [S20](work_simulations/20_acme_commerce_llm_evaluation/README.md) | DATA-1221 | AI release review has no representative evaluation set | `41` |
| [S21](work_simulations/21_acme_commerce_tool_guardrails/README.md) | DATA-1232 | AI assistant requests unauthorized actions | `42` |
| [S22](work_simulations/22_acme_commerce_AI_data_contracts/README.md) | DATA-1240 | AI data contracts | `43` |
| [S23](work_simulations/23_acme_commerce_AI-assisted_data_quality/README.md) | DATA-1251 | AI-assisted data quality | `44` |
| [S24](work_simulations/24_acme_commerce_confidence_and_escalation/README.md) | DATA-1262 | Confidence and escalation | `45` |
| [S25](work_simulations/25_acme_commerce_human-in-the-loop_workflows/README.md) | DATA-1273 | Human-in-the-loop workflow auditability | `46` |
| [S26](work_simulations/26_acme_commerce_agentic_data_operations/README.md) | DATA-1284 | Agentic data operations | `47` |
| [S27](work_simulations/27_acme_commerce_learning_loops_and_AI_operations/README.md) | DATA-1295 | Learning loops and AI operations | `48` |
| [S28](work_simulations/28_acme_commerce_architecture_requirements/README.md) | DATA-1302 | Production architecture requirements | `49` |
| [S29](work_simulations/29_acme_commerce_reliability_slos/README.md) | DATA-1313 | Reliability, SLOs and failure budgets | `50` |
| [S30](work_simulations/30_acme_commerce_security_governance/README.md) | DATA-1324 | Security, governance and AI boundaries | `51` |
| [S31](work_simulations/31_acme_commerce_cost_latency_capacity/README.md) | DATA-1335 | Cost, latency and capacity planning | `52` |
| [S32](work_simulations/32_acme_commerce_incident_response/README.md) | DATA-1346 | Incident response, rollback and recovery | `53` |
| [S33](work_simulations/33_acme_commerce_capstone_architecture_review/README.md) | DATA-1357 | Capstone architecture review / Production Day | `54` |

## Learner workflow

```text
Notebook experiment
      ↓
Independent challenge
      ↓
Open Acme ticket
      ↓
Investigate symptoms + competing hypotheses
      ↓
Change + test + evidence
      ↓
Production / architecture decision
```

## Coverage rule

Every learner notebook is either mapped to one or more scenarios or explicitly marked as a cross-cutting foundation. Every scenario names its preparation notebooks. The graph validator checks both directions and also checks that the mapping appears inside the learner-facing notebook/scenario artifacts.
