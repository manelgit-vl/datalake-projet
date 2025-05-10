#!/bin/bash

# Create Kafka topic
~/kafka/bin/kafka-topics.sh --create --topic ad_stream --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

