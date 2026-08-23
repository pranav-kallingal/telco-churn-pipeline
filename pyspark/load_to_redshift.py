import redshift_connector
import os

#connect to redshift

conn = redshift_connector.connect(
    host = 'telco-workgroup.682919447512.ap-south-1.redshift-serverless.amazonaws.com',
    database = 'dev',
    user = 'admin',
    password = "REDSHIFT_PASSWORD",
    port = 5439,
)

cursor = conn.cursor()

#Truccate table
cursor.execute("""
    TRUNCATE TABLE raw_customers;
""")

#copying s3 date
cursor.execute("""
    COPY public.raw_customers
    FROM 's3://telco-churn-pipeline/raw_parquet/'
    IAM_ROLE '...'
    FORMAT AS PARQUET;
""")

conn.commit()

#verify count
cursor.execute("SELECT COUNT(*) FROM public.raw_customers;")
result = cursor.fetchone()
print(f"Loaded {result[0]} rows into Redshift")

#close connection
cursor.close()
conn.close()
print("table truncated successfully")