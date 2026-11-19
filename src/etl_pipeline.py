from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, sum

# Initialize Spark
spark = SparkSession.builder \
    .appName("SalesETL") \
    .getOrCreate()

# EXTRACT: Read raw CSV
print("=== EXTRACTING RAW DATA ===")
raw_df = spark.read.csv("/app/data/raw_sales.csv", header=True, inferSchema=True)
raw_df.show()

# TRANSFORM: Clean and process
print("=== TRANSFORMING DATA ===")
clean_df = raw_df \
    .dropDuplicates() \
    .dropna(subset=["transaction_id", "date"]) \
    .withColumn("quantity", when(col("quantity").isNull(), lit(0)).otherwise(col("quantity").cast("int"))) \
    .withColumn("price", when(col("price") == "N/A", lit(0.0)).otherwise(col("price").cast("double"))) \
    .withColumn("revenue", col("quantity") * col("price"))

clean_df.show()

# Aggregate: Total revenue per product
print("=== AGGREGATING DATA ===")
final_df = clean_df.groupBy("product") \
    .agg(sum("revenue").alias("total_revenue")) \
    .orderBy(col("total_revenue").desc())

final_df.show()

# LOAD: Write to Parquet
print("=== LOADING TO PARQUET ===")
final_df.write.mode("overwrite").parquet("/app/data/output/clean_sales.parquet")

print("✅ ETL Pipeline Complete!")
spark.stop()

