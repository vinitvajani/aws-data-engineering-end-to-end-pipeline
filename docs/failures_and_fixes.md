# Production Failures & Fixes

## Glue Argument Error

**Error:**
GlueArgumentError: the following arguments are required: --orders-glue-etl

**Root Cause:**
Incorrect use of getResolvedOptions with a custom argument instead of JOB_NAME.

**Fix:**
Replaced:
getResolvedOptions(sys.argv, ['orders-glue-etl'])

With:
getResolvedOptions(sys.argv, ['JOB_NAME'])

---

## Corrupted Partition Error

**Error:**
Path .../year=2025/month=12/Unsaved is a directory, which is not supported

**Root Cause:**
Non-Parquet folder inside partition broke Spark reader.

**Fix:**
- Deleted corrupted folder  
- Enabled recursive input:  
spark.conf.set("mapreduce.input.fileinputformat.input.dir.recursive","true")

---

## Key Learning
S3 is a file system, not a database.  
Partition hygiene is critical for reliable pipelines.