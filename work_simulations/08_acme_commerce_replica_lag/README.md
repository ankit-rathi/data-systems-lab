# DATA-1110 — Replication and consistency

**Level:** L3  
**Primary notebook:** 22 — Replication & Consistency  
**Business symptom:** Inventory reads disagree across regions

## Mission

Explain what the application can observe, distinguish stale reads from lost writes, and choose a consistency strategy under an explicit constraint.


## Your task

1. **Understand the situation:** read the ticket and inspect the evidence.
2. **Find the cause:** write at least two hypotheses and test them.
3. **Make the smallest safe change:** preserve the business constraint and add a regression check.
4. **Prove it:** record before/after evidence and the production decision.

**Do not start by guessing the fix.** Your job is to explain the mechanism with evidence.
## Learner rule

Do not jump from the ticket to the fix. Inspect the evidence, write hypotheses, test them, then make the smallest defensible change.

## Required evidence

- ticket and business impact
- investigation notes and competing hypotheses
- code/query/config change
- tests or measured validation
- Git/PR-style summary
- production implication and prevention idea

This scenario is intentionally deterministic and educational. It is not a production payment, logistics, or security implementation.

## Notebook bridge

**Prepare with these notebooks:**
- **19 — 19_btree_lsm** → [`05_storage_distributed_systems/19_btree_lsm.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/05_storage_distributed_systems/19_btree_lsm.ipynb)
- **20 — 20_wal_recovery** → [`05_storage_distributed_systems/20_wal_recovery.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/05_storage_distributed_systems/20_wal_recovery.ipynb)
- **21 — 21_mvcc_isolation** → [`05_storage_distributed_systems/21_mvcc_isolation.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/05_storage_distributed_systems/21_mvcc_isolation.ipynb)
- **22 — 22_replication_consistency** → [`05_storage_distributed_systems/22_replication_consistency.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/05_storage_distributed_systems/22_replication_consistency.ipynb)
- **23 — 23_partitioning_hashing** → [`05_storage_distributed_systems/23_partitioning_hashing.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/05_storage_distributed_systems/23_partitioning_hashing.ipynb)
- **24 — 24_raft_consensus** → [`05_storage_distributed_systems/24_raft_consensus.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/05_storage_distributed_systems/24_raft_consensus.ipynb)

**Learner rule:** finish the preparation notebooks first, then solve this ticket without using their outputs as the diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.

---

**Check your work:** [Open the reference solution](../../solutions/scenarios/S08.md) — only after you have completed the mission and recorded your evidence.
