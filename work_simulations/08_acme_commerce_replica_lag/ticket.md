# DATA-1110

**Status:** Open  
**Owner:** Acme Commerce Data Platform  
**Priority:** P1 learning simulation  
**Level:** L3

## Reported symptom

Inventory reads disagree across regions

## Request

Investigate the issue, identify the evidence that separates plausible explanations, implement a defensible change, and document how the team should prevent recurrence.

## Constraints

- Core path must run locally with deterministic fixtures.
- Do not assume the ticket names the root cause.
- Preserve useful raw evidence.
- Add regression coverage for the failure you prove.

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
