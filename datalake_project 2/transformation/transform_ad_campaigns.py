from pyspark.sql import SparkSession
import os

# Créer la session Spark
spark = SparkSession.builder.appName("TransformAdCampaigns").getOrCreate()

# Chemins en local
input_path = "file:///" + os.path.abspath("Data_lake/raw/ad_stream")
output_path = "file:///" + os.path.abspath("Data_lake/silver/ad_campaigns")

# Lire les fichiers JSON
df = spark.read.json(input_path)

# Nettoyage et sélection des colonnes utiles
df_clean = df.select("ad_type", "campaign_id", "clicks")

# Agrégation des clics par type de pub et campagne
df_agg = df_clean.groupBy("campaign_id", "ad_type").sum("clicks").withColumnRenamed("sum(clicks)", "clicks")

# Afficher un aperçu (optionnel pour debug)
df_agg.show()
print(f"Nombre de lignes agrégées : {df_agg.count()}")

# Sauvegarde au format Parquet
df_agg.coalesce(1).write.mode("overwrite").parquet(output_path)
