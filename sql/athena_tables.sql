-- Athena external table for processed data

CREATE EXTERNAL TABLE IF NOT EXISTS data_eng_db.orders_processed (
  order_id string,
  product_name string,
  city string,
  quantity int,
  price double,
  status string,
  order_timestamp timestamp,
  order_date date
)
PARTITIONED BY (year int, month int)
STORED AS PARQUET
LOCATION 's3://mycompany-orders/processed/';