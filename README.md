# AWS End-to-End Data Engineering Pipeline

## Overview
Production-ready end-to-end Data Engineering platform built on AWS using a Lakehouse-style architecture.

Event-driven ingestion, serverless orchestration, scalable ETL, analytics-ready warehouse and enterprise monitoring.

---

## Architecture

![Architecture](architecture/architecture.png)

---

## Pipeline Flow

1. Data lands in **Amazon S3 (Raw Zone)**
2. S3 event triggers **AWS Lambda**
3. Lambda starts **AWS Step Functions**
4. Step Functions orchestrates:
   - AWS Glue ETL (Raw → Processed)
   - Amazon Athena CTAS (Processed → Curated)
   - Amazon Redshift Load (Star Schema)
5. Success / Failure metadata stored in **DynamoDB**
6. Logs in **CloudWatch**
7. Alerts via **SNS**

---

## Tech Stack

- Amazon S3 (Data Lake)
- AWS Lambda
- AWS Step Functions
- AWS Glue (PySpark)
- Amazon Athena
- Amazon Redshift
- Amazon DynamoDB
- Amazon CloudWatch
- Amazon SNS
- AWS IAM

---

## Repository Structure

```text
architecture/        -> Architecture diagram
glue_jobs/           -> Glue ETL scripts
stepfunctions/       -> Step Functions orchestration
sql/                 -> Athena & Redshift schemas
docs/                -> System design, security & failure docs
```
---

## Key Features

- Event-driven ingestion  
- Serverless orchestration  
- Fault tolerant ETL with retries  
- Star schema analytics warehouse  
- Production monitoring & alerting  
- Secure IAM design  

---

## Documentation

- System Design → `docs/system_design.md`  
- Failures & Fixes → `docs/failures_and_fixes.md`  
- Security & IAM → `docs/security.md`  

---

## How to Run

1. Upload data to S3 Raw  
2. Pipeline starts automatically  
3. Query analytics in Athena  
4. Build dashboards from Redshift  

---

## Key Learnings

- End-to-end Data Engineering system design  
- AWS serverless data platform  
- ETL orchestration and reliability  
- Analytics warehouse modeling  
- Production debugging  
