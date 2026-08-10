# Telco-Churn-Pipeline

## Description

building an end-to-end batch data pipeline that moves data from CSV to S3 bucket. The pipeline is made with data engineering tools like PySpark, dbt for data processing and transformation, CLI as AWS S3 CLI for data storage and finally Airflow for orchestrating and monitoring.

## Tools
1. pyspark
2. dbt
3. aws s3 cli
4. airflow
5. Duckdb
6. Redshift serverless

## Architecture 
Raw CSV → A batch file is send by user to path
PySpark schema validation → data is validate here.
Parquet conversion →  file is converted to parquet file and stored 
JSON schema contract → a json contract file is created to store data schema for future use and tracking changes
dbt staging (stg_customers) → raw data is loaded to stg table
dbt marts (churn by contract, revenue at risk, senior citizen churn) → business metrics are calculated and stored in dbt marts
Redshift Serverless → final mart tables loaded for analytics

