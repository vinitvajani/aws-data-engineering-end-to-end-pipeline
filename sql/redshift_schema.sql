-- Redshift Star Schema (Corrected)

CREATE TABLE dim_product (
  product_sk BIGINT IDENTITY(1,1),
  product_name VARCHAR(255),
  PRIMARY KEY (product_sk)
);

CREATE TABLE dim_city (
  city_sk BIGINT IDENTITY(1,1),
  city_name VARCHAR(255),
  PRIMARY KEY (city_sk)
);

CREATE TABLE dim_date (
  date_sk BIGINT IDENTITY(1,1),
  order_date DATE,
  year INT,
  month INT,
  day INT,
  PRIMARY KEY (date_sk)
);

CREATE TABLE fact_orders (
  order_id VARCHAR(50),
  product_sk BIGINT,
  city_sk BIGINT,
  date_sk BIGINT,
  quantity INT,
  price DOUBLE PRECISION,
  status VARCHAR(50)
);