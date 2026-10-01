# DATA-1120 — Event stream backlog

**Level:** L2 → L3  
**Primary notebooks:** 25–30 — Big Data, Streaming & Lakehouse  
**Company area:** Acme Commerce web/app events

## Business symptom

The operations team reports that the live sales-events dashboard is falling further behind during a campaign. Some events appear late, and after a consumer restart the dashboard occasionally shows a count higher than the source export.

The ticket does **not** tell you whether the problem is execution, partitioning, time semantics, delivery semantics, or storage layout.

## Mission

Work through the incident as a sequence of hypotheses:

1. Is the workload simply taking longer than the arrival rate?
2. Is partitioning creating a hot key and a straggler?
3. Are late events being handled consistently?
4. Is replay creating duplicate downstream effects?
5. Is the table/storage layer amplifying operational cost?

The learner should not fix all five possibilities. The evidence should narrow the problem before the change is made.


## Your task

1. **Understand the situation:** read the ticket and inspect the evidence.
2. **Find the cause:** write at least two hypotheses and test them.
3. **Make the smallest safe change:** preserve the business constraint and add a regression check.
4. **Prove it:** record before/after evidence and the production decision.

**Do not start by guessing the fix.** The ticket gives you the situation, not the diagnosis.
## Scenario progression

- **25:** reason about the execution graph.
- **26:** measure partition balance and skew.
- **27:** inspect log/offset behavior.
- **28:** reason about late events and windows.
- **29:** reproduce replay and make the downstream effect idempotent.
- **30:** connect the stream output to append-only files, metadata and compaction.

## Evidence target

Produce an incident note, a small deterministic reproduction, tests/measurements, a change proposal and a PR-style summary. Record which hypotheses were rejected and why.

## Notebook bridge

**Prepare with these notebooks:**
- **25 — Spark Execution & Lazy Evaluation** → [`06_streaming_lakehouse/25_spark_execution_lazy.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/25_spark_execution_lazy.ipynb)
- **26 — Shuffle, Partitioning & Skew** → [`06_streaming_lakehouse/26_shuffle_partitioning_skew.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/26_shuffle_partitioning_skew.ipynb)
- **27 — Kafka Fundamentals & Partitioned Logs** → [`06_streaming_lakehouse/27_kafka_partitioned_logs.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/27_kafka_partitioned_logs.ipynb)
- **28 — Event Time, Processing Time & Windows** → [`06_streaming_lakehouse/28_event_time_processing_time.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/28_event_time_processing_time.ipynb)
- **29 — Delivery Semantics, Replay & Offsets** → [`06_streaming_lakehouse/29_delivery_semantics_offsets.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/29_delivery_semantics_offsets.ipynb)
- **30 — Lakehouse Tables, Compaction & Schema Evolution** → [`06_streaming_lakehouse/30_lakehouse_compaction_schema.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/06_streaming_lakehouse/30_lakehouse_compaction_schema.ipynb)

**Learner rule:** finish the preparation notebooks first, then solve this ticket without using their outputs as the diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.

---

**Check your work:** [Open the reference solution](../../solutions/scenarios/S09.md) — only after you have completed the mission and recorded your evidence.
