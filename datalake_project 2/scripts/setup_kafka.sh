#!/bin/bash

# Démarrer Zookeeper et Kafka depuis ton dossier personnel
~/kafka/bin/zookeeper-server-start.sh ~/kafka/config/zookeeper.properties &
sleep 5
~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties
