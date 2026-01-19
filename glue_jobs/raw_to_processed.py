import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import trim, initcap, lower, col, to_timestamp, year, month, dayofmonth, to_date

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
df = spark.read.table("data_eng_db.orders_raw_2026_01_csv")
df = df.filter(df.order_id.isNotNull())
df = df.withColumn("product_name", trim(df["product_name"]))
df = df.withColumn("product_name", initcap(df["product_name"]))
df = df.withColumn("city", trim(df["city"]))
df = df.withColumn("city", initcap(df["city"]))
df = df.filter(df["quantity"] > 0)
df = df.withColumn("price", col("price").cast("double"))
df = df.filter(df["price"] > 0)
df = df.withColumn("status", lower(df["status"]))
df = df.withColumn("order_timestamp", to_timestamp(df["order_timestamp"], "yyyy-MM-dd'T'HH:mm:ss"))
df = df.withColumn("order_date", to_date(col("order_timestamp"))) \
       .withColumn("year", year(col("order_timestamp"))) \
       .withColumn("month", month(col("order_timestamp"))) \
       .withColumn("day", dayofmonth(col("order_timestamp")))
df.show()
df.write.mode("overwrite").partitionBy("year","month").parquet("s3://mycompany-orders/processed/")
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
job.commit()
