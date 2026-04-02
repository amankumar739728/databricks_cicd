# Databricks notebook source
import dlt

@dlt.table(name="customers_gold")
def gold():
    df = dlt.read("customers_silver")
    return df.groupBy("country").count()