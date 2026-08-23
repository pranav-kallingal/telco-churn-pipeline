# Telco Customer Churn — End-to-End Data Pipeline

## Business Problem
Identify which customer segments are churning and quantify the monthly revenue at risk, enabling the analytics team to take targeted retention actions.

## Architecture
Raw CSV → PySpark (Validation + Parquet) → AWS S3 (Data Lake) → Redshift Serverless (Data Warehouse) → dbt (Staging + Marts) → BI / Analytics


## Pipeline Flow
1. **CSV Ingestion** — Raw CSV file lands in the collection path
2. **PySpark Validation** — Schema validation, null checks, row count verification
3. **Parquet Conversion** — CSV converted to columnar Parquet format for performance
4. **JSON Schema Contract** — Schema contract generated for data governance and change tracking
5. **S3 Upload (boto3)** — Parquet files uploaded to AWS S3 Data Lake
6. **Redshift COPY** — Bulk load from S3 into Redshift raw staging table
7. **dbt Transformations** — Staging layer cleans raw data; Mart layer builds business metrics
8. **Airflow Orchestration** — All steps orchestrated as a DAG with task dependencies

## dbt Models
| Model | Description |
|-------|-------------|
| `stg_customers` | Cleaned and type-cast staging layer |
| `mart_churn_by_contract` | Churn rate by contract type |
| `mart_churn_by_internet` | Churn rate by internet service |
| `mart_revenue_at_risk` | Monthly revenue at risk from churned customers |
| `mart_senior_citizen_churn` | Churn analysis for senior vs non-senior customers |

## Tools & Technologies
| Tool | Purpose |
|------|---------|
| PySpark | Schema validation, CSV → Parquet conversion |
| AWS S3 | Data Lake storage |
| AWS Redshift Serverless | Cloud Data Warehouse (OLAP) |
| dbt | SQL transformations (ELT) |
| Apache Airflow (Docker) | Pipeline orchestration |
| boto3 | Programmatic S3 uploads |
| DuckDB | Local development database |

## How to Run
1. Place raw CSV in `data/raw/`
2. Trigger the Airflow DAG (`Telco-pipeline`)
3. Pipeline validates → converts → uploads to S3 → loads into Redshift → runs dbt models
4. Query final mart tables in Redshift for analytics