FROM apache/airflow:2.7.1-python3.10
USER root
COPY dags /opt/airflow/dags
COPY ../ingestion /opt/airflow/ingestion
COPY ../transformation /opt/airflow/transformation
RUN pip install kafka-python pyspark
