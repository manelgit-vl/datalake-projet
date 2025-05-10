# Datalake Project

## Structure

- Ingestion via Kafka
- Transformation with PySpark
- DAG orchestration with Airflow

## Usage

1. Start Kafka: `bash scripts/setup_kafka.sh`
2. Create Topic: `bash scripts/kafka-topics.sh`
3. Launch Producer: `python ingestion/kafka_producer.py`
4. Start Ingestion: `python ingestion/read_ad_stream.py`
5. Run Transformations: `python transformation/run_all_transformations.py`
