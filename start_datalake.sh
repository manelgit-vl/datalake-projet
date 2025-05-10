#!/bin/bash

echo "📦 Activation de l'environnement de projet..."

# 1. Aller dans le dossier du projet
cd /mnt/c/Users/manel/Downloads/datalake_project\ 2/datalake_project\ 2 || exit 1

# 2. Démarrer Airflow (si installé en local, adapte selon ton installation Docker si besoin)
echo "🚀 Démarrage d'Airflow Webserver et Scheduler..."
airflow db init
airflow webserver -p 8080 &
sleep 10
airflow scheduler &

# 3. Lancer toutes les transformations Spark
echo "🔄 Exécution des transformations..."
python3 transformation/run_all_transformations.py

# 4. Lancer l’API Flask
echo "🌐 Démarrage de l'API Flask..."
cd api
python3 app.py
