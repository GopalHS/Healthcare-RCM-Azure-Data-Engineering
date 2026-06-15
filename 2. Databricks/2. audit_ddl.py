# Databricks notebook source
# Storage key redacted for public GitHub upload.
# In production, retrieve this from Azure Key Vault / Databricks Secrets.
storage_key = "<REDACTED_STORAGE_KEY>"

spark.conf.set(
    "fs.azure.account.key.hrcmstorage.dfs.core.windows.net",
    storage_key
)

spark.sparkContext._jsc.hadoopConfiguration().set(
    "fs.azure.account.key.hrcmstorage.dfs.core.windows.net",
    storage_key
)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW CATALOGS;

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG spark_catalog;

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

spark.conf.set(
    "fs.azure.account.key.hrcmstorage.dfs.core.windows.net",
    storage_key
)

schema = StructType([
    StructField("data_source", StringType(), True),
    StructField("tablename", StringType(), True),
    StructField("numberofrowscopied", IntegerType(), True),
    StructField("watermarkcolumnname", StringType(), True),
    StructField("loaddate", TimestampType(), True)
])

df = spark.createDataFrame([], schema)

audit_path = "abfss://config@hrcmstorage.dfs.core.windows.net/audit/load_logs"

df.write.format("delta").mode("overwrite").save(audit_path)

# COMMAND ----------

display(spark.read.format("delta").load(audit_path))

# COMMAND ----------

display(spark.read.format("delta").load("abfss://config@hrcmstorage.dfs.core.windows.net/audit/load_logs"))