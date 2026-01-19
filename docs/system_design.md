# System Design – AWS End-to-End Data Engineering Pipeline

## Problem Statement
Build a scalable, reliable data platform to ingest order data and provide analytics-ready datasets for business intelligence.

---

## High Level Architecture

Source Systems  
→ Amazon S3 (Raw)  
→ AWS Glue (ETL)  
→ Amazon S3 (Processed / Curated)  
→ Amazon Athena  
→ Amazon Redshift  

---

## Design Decisions

### Why Amazon S3 as Data Lake
- Infinite scalability  
- Low cost storage  
- Decouples storage & compute  
- Supports Parquet for analytics  

### Why AWS Glue
- Serverless Spark  
- Automatic scaling  
- Native integration with S3 & Athena  
- Built-in Data Catalog  

### Partition Strategy
Partitioned by:
- year  
- month  

Enables:
- Partition pruning  
- Faster queries  
- Lower Athena & Redshift cost  

### Data Quality Strategy
- Remove null order_id  
- Enforce positive quantity & price  
- Standardize text fields  
- Cast datatypes  
- Validate timestamps  

### Failure Handling
- Idempotent overwrite of partitions  
- Recursive input enabled to handle junk folders  
- Logging and retries  

### Cost Optimization
- Parquet format  
- Partition pruning  
- Serverless compute  
- On-demand Redshift loading  

---

## Analytics Design

### Fact Table
fact_orders

### Dimension Tables
- dim_product  
- dim_city  
- dim_date  

Star schema used for BI workloads.

---

## Security
- IAM roles for Glue, Athena, Redshift  
- Least privilege access  
- S3 bucket policies  