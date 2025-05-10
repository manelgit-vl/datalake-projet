from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Définitions de base du DAG
default_args = {
    'owner': 'manel',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'datalake_pipeline',
    default_args=default_args,
    description='Pipeline Datalake local sans HDFS',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
)

# 1. Ingestion (simulée par script Kafka)
ingestion = BashOperator(
    task_id='ingestion_task',
    bash_command='python3 ingestion/read_ad_stream.py',
    dag=dag
)

# 2. Transformation (run tous les scripts PySpark)
transformation = BashOperator(
    task_id='transformation_task',
    bash_command='python3 transformation/run_all_transformations.py',
    dag=dag
)

# 3. Export (API déjà mise en place avec Flask, ici on peut juste signaler que le dataset final est prêt)
export = BashOperator(
    task_id='export_task',
    bash_command='echo "Dataset final prêt dans Data_lake/gold/final_dataset"',
    dag=dag
)

# Dépendances
ingestion >> transformation >> export
