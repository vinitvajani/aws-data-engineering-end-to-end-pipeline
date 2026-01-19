# Security & IAM Design

## Overview
Security is enforced using least privilege IAM roles and bucket policies across the pipeline.

---

## IAM Roles

### Lambda Role
- Read access to S3 Raw bucket  
- Start Step Functions execution  
- Write logs to CloudWatch  

### Step Functions Role
- Start Glue jobs  
- Run Athena queries  
- Execute Redshift Data API  
- Write to DynamoDB  
- Publish to SNS  

### Glue Role
- Read S3 Raw  
- Write S3 Processed  
- Read Glue Data Catalog  
- Write logs to CloudWatch  

### Athena Role
- Read S3 Processed  
- Write S3 Curated  
- Write query results  

### Redshift Role
- Read S3 Curated  
- Load data using COPY  
- Query analytics tables  

---

## S3 Bucket Policies

- Raw, Processed, Curated buckets allow access only to:
  - Glue  
  - Athena  
  - Redshift  
  - Step Functions  
- Public access blocked  

---

## Security Best Practices

- IAM least privilege  
- Encryption at rest (S3, Redshift)  
- Encryption in transit  
- CloudWatch audit logs  
- SNS alerts for failures  