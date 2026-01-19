"""
Processed → Curated Glue Job

This job reads cleaned data from the processed layer,
applies business transformations and builds analytics-ready tables.

Used for:
- Fact Orders table
- Dimension tables (Product, City, Date)

This stage is documented in system_design.md and implemented using Athena/Redshift.
"""