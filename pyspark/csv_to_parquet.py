import os, sys
from pyspark.sql import SparkSession

output_path = "/Users/apple/Desktop/project-main/data/parquet"
spark = SparkSession.builder.appName("Telco").getOrCreate()
path_file = "/Users/apple/Desktop/project-main/data/raw/Telco-Customer-Churn.csv"
df = spark.read.option("header", True).option("inferSchema", True).csv(path_file)
df.write.mode("overwrite").parquet(output_path)

print("csv file is converted to parquet file")