from pyspark.sql import SparkSession 
import os

spark = SparkSession.builder.appName("ExplorerSilver").getOrCreate()

# Définir les chemins absolus en mode local
base_path = os.path.abspath("Data_lake/silver")

datasets = {
    "ad_campaigns": f"file:///{base_path}/ad_campaigns",
    "social_media": f"file:///{base_path}/social_media",
    "web_logs": f"file:///{base_path}/web_logs"
}

for name, path in datasets.items():
    print(f"\n🔍 Dataset: {name}")
    try:
        df = spark.read.parquet(path)
        df.printSchema()
        df.show(5, truncate=False)
    except Exception as e:
        print(f"❌ Erreur lecture de {name} : {e}")

# Ajout de la lecture du dataset gold
print("\n🔍 Dataset: final_dataset")
try:
    gold_path = "file:///" + os.path.abspath("Data_lake/gold/final_dataset")
    df_gold = spark.read.parquet(gold_path)
    df_gold.printSchema()
    df_gold.show(5, truncate=False)
except Exception as e:
    print(f"❌ Erreur lecture de final_dataset : {e}")
