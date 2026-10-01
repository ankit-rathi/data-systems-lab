# DATA-1110 — Replication and consistency

**Level:** L3  
**Primary notebook:** 22 — Replication & Consistency  
**Business symptom:** Inventory reads disagree across regions

## Mission

Explain what the application can observe, distinguish stale reads from lost writes, and choose a consistency strategy under an explicit constraint.

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

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
