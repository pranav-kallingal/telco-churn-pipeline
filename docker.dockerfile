FROM apache/airflow:3.0.6

USER root
RUN apt-get update && apt-get install -y default-jdk && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64

USER airflow
RUN pip install pyspark==3.5.1 dbt-duckdb==1.9.1