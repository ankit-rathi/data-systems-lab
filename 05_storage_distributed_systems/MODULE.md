# Module 05 — Storage Internals & Distributed Systems

**Purpose:** Build accurate mental models for how databases store, recover, isolate, replicate and distribute state.

**Prerequisites:** Notebooks 05–14, especially indexes, transactions, data modeling, pipeline checkpoints and quality gates.

| # | Notebook | Core experiment | Level |
|---:|---|---|---|
| 19 | B-Trees & LSM Trees | Ordered index vs buffered sorted runs and compaction | L1/L2 |
| 20 | Write-Ahead Logging & Recovery | Replay committed changes after a crash | L2/L3 |
| 21 | MVCC & Transaction Isolation | Snapshot visibility and stale-write conflict | L2/L3 |
| 22 | Replication & Consistency | Leader/follower lag and quorum intuition | L2/L3 |
| 23 | Partitioning & Consistent Hashing | Key movement when nodes change | L2/L3 |
| 24 | Consensus, Raft & Failure Models | Majority quorum under node/network failures | L2/L3 |

## Module arc

```text
Index → Log → Versions → Replicas → Partitions → Consensus
```

All notebooks use deterministic standard-library simulations. These are explicitly teaching models, not implementations or performance benchmarks of production databases.
