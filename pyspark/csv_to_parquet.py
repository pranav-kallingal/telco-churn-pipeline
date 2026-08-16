import os, sys
from pyspark.sql import SparkSession

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join(BASE_DIR, "data", "parquet")

path_file = os.path.join(BASE_DIR, "data", "raw", "Telco-Customer-Churn.csv")


spark = SparkSession.builder.appName("Telco").getOrCreate()
df = spark.read.option("header", True).option("inferSchema", True).csv(path_file)
df.write.mode("overwrite").parquet(output_path)

print("csv file is converted to parquet file")