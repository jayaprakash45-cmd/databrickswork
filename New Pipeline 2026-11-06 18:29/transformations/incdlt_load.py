import dlt

rules  = {
    "rule1" : "OrderID IS NOT NULL",
    "rule2" : "Customer IS NOT NULL",
    "rule3" : "Quantity >0",
    "rule4" : "Price >0"
}

@dlt.table(
    name="inc_table"
)
@dlt.expect_all_or_fail(rules)
def inc_table():
    df = spark.readStream.format("cloudFiles").option("cloudFiles.format","csv").load("/Volumes/catalog_intrvw/source/orders_vol")
    return df

