import boto3
import os

s3_client = boto3.client('s3')

bucket = 'telco-churn-pipeline'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parquet_dir = os.path.join(BASE_DIR, 'data', 'parquet')


for filename in os.listdir(parquet_dir):
    if filename.startswith('.') or filename.startswith('_'):
        continue

    s3_key = f"raw_parquet/{filename}"
    local_path = f"{parquet_dir}/{filename}"
    s3_client.upload_file(Filename=local_path, Bucket=bucket, Key=s3_key)

    print(f"Uploaded : {s3_key} -> s3://{bucket}/{s3_key}")


print("parquet files are uploaded to S3")