# DATA-1120 — Event stream backlog

**Priority:** P1 learning simulation  
**Status:** Open  
**Owner:** Acme Commerce Data Platform

## Reported symptom

During the campaign, the live sales-events dashboard is falling behind. Operators also report late events and occasional over-counting after a consumer restart.

## Constraints

- Keep the core reproduction deterministic and local.
- Do not assume the root cause is "Kafka" or "Spark".
- Preserve raw events so the business result can be reconstructed.
- A fix must explain both freshness and correctness implications.

## Notebook bridge

**Prepare with these notebooks:**
- **25 — Spark Execution & Lazy Evaluation** → [`06_streaming_lakehouse/25_spark_execution_lazy.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/25_spark_execution_lazy.ipynb)
- **26 — Shuffle, Partitioning & Skew** → [`06_streaming_lakehouse/26_shuffle_partitioning_skew.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/26_shuffle_partitioning_skew.ipynb)
- **27 — Kafka Fundamentals & Partitioned Logs** → [`06_streaming_lakehouse/27_kafka_partitioned_logs.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/27_kafka_partitioned_logs.ipynb)
- **28 — Event Time, Processing Time & Windows** → [`06_streaming_lakehouse/28_event_time_processing_time.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/28_event_time_processing_time.ipynb)
- **29 — Delivery Semantics, Replay & Offsets** → [`06_streaming_lakehouse/29_delivery_semantics_offsets.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/29_delivery_semantics_offsets.ipynb)
- **30 — Lakehouse Tables, Compaction & Schema Evolution** → [`06_streaming_lakehouse/30_lakehouse_compaction_schema.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/30_lakehouse_compaction_schema.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
