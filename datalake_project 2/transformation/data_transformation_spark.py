from pyspark.sql import SparkSession

def init_spark():
    spark = SparkSession.builder         .appName("Data Transformation")         .getOrCreate()
    return spark
