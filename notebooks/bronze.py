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



# Databricks notebook source
import dlt
import os

# This will be injected per environment via databricks.yml pipeline config
input_path = spark.conf.get("input_path")

@dlt.table(name="customers_bronze")
def bronze():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .load(input_path)
    )