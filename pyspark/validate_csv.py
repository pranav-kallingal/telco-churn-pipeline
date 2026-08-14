import os, sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


spark = SparkSession.builder.appName("Telco").getOrCreate()
path_file = "/Users/apple/Desktop/project-main/data/raw/Telco-Customer-Churn.csv"
df = spark.read.option("header", True).option("inferSchema", True).csv(path_file)
expected_cols = ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 
                 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                   'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 
                   'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn']

def column_check(df) :  
    if len(df.columns) == 21 and set(expected_cols) == set(df.columns):
        pass
    else :
        print("unexpected columns detected : ", set(expected_cols) - set(df.columns))
        sys.exit(1)

    if df.filter(col("customerID").isNull()).count() == 0:
        pass
    else : 
        print("null values found in customerID ", df.filter(col("customerID").isNull()).count())
        sys.exit(1)

    if df.cache().count() > 0:
        pass
    else : 
        sys.exit(1)
    
    return print("Dataset is good to process"), df

column_check(df)




