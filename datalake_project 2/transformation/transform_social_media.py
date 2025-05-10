from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import os

spark = SparkSession.builder.appName("TransformSocialMedia").getOrCreate()

schema = StructType([
    StructField("platform", StringType(), True),
    StructField("likes", IntegerType(), True),
    StructField("shares", IntegerType(), True)
])

input_path = "file:///" + os.path.abspath("Data_lake/raw/social_media")
output_path = "file:///" + os.path.abspath("Data_lake/silver/social_media")

df = spark.read.schema(schema).json(input_path)
df_clean = df.dropna()
df_clean.write.mode("overwrite").parquet(output_path)
