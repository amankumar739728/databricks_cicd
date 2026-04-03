#code for running inside created dlt pipeline as path is hardcoded
# import dlt

# @dlt.table(name="customers_bronze")
# def bronze():
#     return (
#         spark.readStream
#         .format("cloudFiles")
#         .option("cloudFiles.format", "csv")
#         .load("/Workspace/Users/aman.kumar@gyansys.com/databricks_cicd/mnt/data/input/Customers.csv")
#     )



# import dlt
# import os

# # This will be injected per environment via databricks.yml pipeline config
# input_path = spark.conf.get("input_path")

# @dlt.table(name="customers_bronze")
# def bronze():
#     return (
#         spark.readStream
#         .format("cloudFiles")
#         .option("cloudFiles.format", "csv")
#         .load(input_path)
#     )



import dlt
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

# This will be injected per environment via databricks.yml pipeline config
input_path = spark.conf.get("input_path")

# Define schema with id as integer
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("email", StringType(), True),
    StructField("country", StringType(), True),
    StructField("amount", DoubleType(), True)
])

@dlt.table(name="customers_bronze")
def bronze():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .schema(schema)
        .load(input_path)
    )