from pyspark.sql import SparkSession
import json

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
in_path = os.path.join(BASE_DIR, "data", "parquet")
out_path = os.path.join(BASE_DIR, "data", "json", "telco_contract.json")

spark = SparkSession.builder.appName("Telco-JSON").getOrCreate()
parquet_df = spark.read.parquet(in_path)
parquet_col = dict(parquet_df.dtypes)

with open(out_path, "w") as f:
    json.dump(parquet_col, f, indent=4)

print("File is created")

