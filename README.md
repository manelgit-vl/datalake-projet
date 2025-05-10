# 🧠 Projet Datalake Local (sans HDFS)

Ce projet met en place un pipeline complet de données en local, sans dépendre de Hadoop (HDFS), en utilisant **Apache Spark**, **Airflow**, et une **API Flask**. Il simule un scénario réel de traitement de données marketing.

---

## 🚀 Objectif

Traiter et exposer via une API des données issues de plusieurs sources marketing : campagnes publicitaires, réseaux sociaux, logs web.

---

## 📁 Structure du projet

```
datalake_project/
├── Data_lake/
│   ├── raw/           → Données brutes (JSON)
│   ├── silver/        → Données nettoyées (parquet)
│   └── gold/          → Données finales combinées (parquet)
│
├── ingestion/
│   └── read_ad_stream.py
├── transformation/
│   ├── transform_ad_campaigns.py
│   ├── transform_social_media.py
│   ├── transform_web_logs.py
│   ├── transform_gold.py
│   └── run_all_transformations.py
├── api/
│   └── app.py             → API Flask pour exposer les données finales
├── airflow_env/
│   └── dags/
│       └── datalake_pipeline.py → DAG Airflow
├── start_datalake.sh      → Script shell pour tout lancer automatiquement
├── docker-compose.yml     → (optionnel, non utilisé ici)
└── README.md
```

---

## 🛠️ Étapes humaines du projet

### 1. 🔁 Ingestion

Les fichiers JSON sont simulés comme des flux de données dans `Data_lake/raw`. L'ingestion est faite manuellement via des scripts Python (pas de Kafka réel).

### 2. 🧹 Transformation

Chaque type de donnée (ad campaigns, social media, web logs) est transformé et nettoyé avec **PySpark**, puis écrit au format **parquet** dans `Data_lake/silver`.

### 3. 🔗 Agrégation (gold layer)

Les données sont combinées avec une stratégie personnalisée : comme aucune colonne n'était commune entre les 3 sources, une clé factice `join_key` a été ajoutée pour effectuer une **jointure croisée** et créer un jeu de données complet.

### 4. 🌐 API Flask

Une **API Flask** a été créée pour exposer les données finales (`gold/final_dataset`) au format JSON via l'URL `http://localhost:5000/data`.

### 5. 📊 Orchestration avec Airflow

Un DAG Airflow (`datalake_pipeline`) orchestre automatiquement les étapes : ingestion → transformation → export.

### 6. ▶️ Lancement automatisé

Un **script shell unique** permet de tout lancer automatiquement en une ligne (`./start_datalake.sh`).

---

## ✅ Lancer le projet automatiquement

```bash
bash run_pipeline.sh
```

**Cela va :**

* Activer l'environnement Python
* Lancer les scripts de transformation
* Démarrer l'API Flask
* Démarrer Airflow webserver + scheduler

---

## 🌐 Utilisation de l’API

```bash
cd api
python3 app.py
```

Puis ouvre ton navigateur et visite : [http://localhost:5000/data](http://localhost:5000/data)

---

## 🛠️ Technologies

* **Python 3**
* **PySpark**
* **Pandas**
* **Airflow**
* **Flask**
* **JSON / Parquet**
* **VS Code + Terminal WSL**

---

## 📸 Pour le rendu final

Fais des **captures d’écran** de :

* L’exécution des scripts de transformation dans le terminal
* Le résultat JSON dans le navigateur (`http://localhost:5000/data`)
* L’interface Airflow avec le DAG en succès
* La structure du dossier dans VS Code

---

##  Auteur : Ossama Louridi & Manel ZERGUIT 
---


