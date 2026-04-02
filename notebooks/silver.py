import dlt

@dlt.table(name="customers_silver")

@dlt.expect("valid_id", "id IS NOT NULL")
@dlt.expect("valid_country", "country IS NOT NULL")
@dlt.expect_or_drop("valid_email", "email LIKE '%@%'")

def silver():
    return dlt.read("customers_bronze").dropDuplicates()