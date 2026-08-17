from airflow import DAG
import datetime
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="Telco-pipeline",
    start_date=datetime.datetime(2020, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    extractVal_task = BashOperator(
        task_id="load-data-validate",
        bash_command="python3 /opt/airflow/project/pyspark/validate_csv.py"
    )

    convert_parquet = BashOperator(
        task_id="convert-parquet",
        bash_command="python3 /opt/airflow/project/pyspark/csv_to_parquet.py"
    )

    json_contract = BashOperator(
        task_id="json-contract",
        bash_command="python3 /opt/airflow/project/pyspark/create_json_contract.py"
    )
    dbt_run = BashOperator(
        task_id="dbt-run",
        bash_command="cd /opt/airflow/project/telco_dbt && dbt run --profiles-dir . --exclude example"
    )

    extractVal_task >> convert_parquet >> json_contract >> dbt_run