# 📊 Datalake Project – Pipeline de Données Big Data

Ce projet met en place un pipeline **Data Lake** complet en local avec **Spark**, **Airflow**, et une **API Flask** pour exposer les données finales. Il suit l’architecture classique **Bronze → Silver → Gold**.

---

## 📁 Structure du Projet

datalake_project/
├── Data_lake/
│ ├── raw/ # Données brutes (ad_stream, social_media, web_logs)
│ ├── silver/ # Données transformées
│ └── gold/ # Dataset final (agrégation)
├── ingestion/
│ └── read_ad_stream.py
├── transformation/
│ ├── transform_ad_campaigns.py
│ ├── transform_social_media.py
│ ├── transform_web_logs.py
│ ├── transform_gold.py
│ └── run_all_transformations.py
├── api/
│ └── app.py # API Flask pour exposer les données finales
├── airflow_env/
│ └── dags/
│ └── datalake_pipeline.py # DAG Airflow
├── run_pipeline.sh # Script shell pour tout lancer automatiquement
└── README.md

---

## ✅ Étapes du Pipeline (Relance le stream, Exécute les transformations, Met à jour le dataset final, Lance l’API Flask)

### 1. ⚙️ Setup environnement local
- Installation de Spark, Airflow, Flask
- Exécution possible avec un seul script : `run_pipeline.sh`

### 2. 📥 Ingestion
- `read_ad_stream.py` simule un flux de données JSON ligne par ligne dans `raw/ad_stream`

### 3. 🗃️ Zone Bronze (raw)
- Données stockées dans `Data_lake/raw/` : ad_stream, social_media, web_logs

### 4. 🔁 Transformation (Silver)
- Nettoyage / structuration avec Spark :
  - `transform_ad_campaigns.py`
  - `transform_social_media.py`
  - `transform_web_logs.py`

### 5. 🧱 Modélisation finale (Gold)
- `transform_gold.py` fusionne les données Silver avec une `join_key`
- Résultat écrit dans `Data_lake/gold/final_dataset`

### 6. 🚀 API Flask
- Expose les données finales via `api/app.py`
- Endpoint : `http://localhost:5000/data`

### 7. 📊 Orchestration avec Airflow
- DAG dans `airflow_env/dags/datalake_pipeline.py`
- Exécute automatiquement : ingestion → transformation → export

---

## 🔁 Lancement Automatisé

Depuis le dossier `datalake_project` :

```bash
bash run_pipeline.sh


🌐 Utilisation de l’API
cd api
python3 app.py
Puis visite : http://localhost:5000/data

🛠️ Technologies
Python 3

PySpark

Pandas

Airflow

Flask

JSON / Parquet

VS Code + Terminal WSL

✍️ Réalisé par : Ossama LOURIDI & Manel ZERGUIT
