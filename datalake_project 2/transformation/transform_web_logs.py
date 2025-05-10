from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.appName("TransformWebLogs").getOrCreate()

input_path = "file:///" + os.path.abspath("Data_lake/raw/web_logs/web_logs.json")
output_path = "file:///" + os.path.abspath("Data_lake/silver/web_logs")

# Charger les données JSON
df = spark.read.json(input_path)

# Sélectionner les colonnes réellement présentes dans le fichier
df_clean = df.select("ip", "timestamp", "url")

# Écrire au format Parquet
df_clean.write.mode("overwrite").parquet(output_path)
