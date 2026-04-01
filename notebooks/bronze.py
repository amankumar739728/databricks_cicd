import dlt

@dlt.table(name="customers_bronze")
def bronze():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .load("/mnt/data/input")
    )