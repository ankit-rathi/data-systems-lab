# DATA-1051

**Status:** Open  
**Owner:** Acme Commerce Data Platform  
**Priority:** P1 learning simulation  
**Level:** L1→L2

## Reported symptom

Daily sales feed broke after a supplier API changed a field from total_amount to amount

## Request

Investigate the issue, identify the evidence that separates plausible explanations, implement a defensible change, and document how the team should prevent recurrence.

## Constraints

- Core path must run locally with deterministic fixtures.
- Do not assume the ticket names the root cause.
- Preserve useful raw evidence.
- Add regression coverage for the failure you prove.

## Notebook bridge

**Prepare with these notebooks:**
- **02 — Files, JSON and APIs** → [`01_data_fundamentals/02_files_json_apis.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/01_data_fundamentals/02_files_json_apis.ipynb)
- **03 — CSV vs JSON vs Parquet** → [`01_data_fundamentals/03_csv_json_parquet.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/01_data_fundamentals/03_csv_json_parquet.ipynb)
- **04 — Apache Arrow and Columnar Memory** → [`01_data_fundamentals/04_arrow_columnar_memory.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/01_data_fundamentals/04_arrow_columnar_memory.ipynb)
- **11 — 11_api_parquet_duckdb** → [`03_reliable_data_engineering/11_api_parquet_duckdb.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/03_reliable_data_engineering/11_api_parquet_duckdb.ipynb)
- **15 — 15_data_contracts** → [`04_quality_observability_orchestration/15_data_contracts.ipynb`](https://github.com/ankit-rathi/data-systems-lab/blob/main/04_quality_observability_orchestration/15_data_contracts.ipynb)

**Learner rule:** use the notebooks to understand the mechanism and run the experiments, then enter this ticket independently. Do not treat the notebook output as the scenario diagnosis.

**Evidence handoff:** carry forward your prediction, relevant measurements, failure reproduction and verification idea; the scenario should add ambiguity, business constraints and a production decision.
