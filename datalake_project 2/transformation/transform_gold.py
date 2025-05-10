from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
import os

# Initialiser Spark
spark = SparkSession.builder.appName("TransformGold").getOrCreate()

# Définir les chemins absolus des fichiers Silver
ads_path = "file:///" + os.path.abspath("Data_lake/silver/ad_campaigns")
social_path = "file:///" + os.path.abspath("Data_lake/silver/social_media")
logs_path = "file:///" + os.path.abspath("Data_lake/silver/web_logs")
output_path = "file:///" + os.path.abspath("Data_lake/gold/final_dataset")

# Lire les fichiers Parquet
df_ads = spark.read.parquet(ads_path)
df_social = spark.read.parquet(social_path)
df_logs = spark.read.parquet(logs_path)

# Ajouter une colonne join_key = 1 à chaque DataFrame
df_ads = df_ads.withColumn("join_key", lit(1))
df_social = df_social.withColumn("join_key", lit(1))
df_logs = df_logs.withColumn("join_key", lit(1))

# Effectuer une jointure factice sur join_key
df_joined = df_ads.join(df_social, on="join_key", how="inner") \
                  .join(df_logs, on="join_key", how="inner") \
                  .drop("join_key")  # On supprime la colonne inutile après jointure

# Écrire le résultat dans le dossier Gold
df_joined.write.mode("overwrite").parquet(output_path)
