-- Query Optimisation Lab: seed script
-- Usage: createdb shop && psql -d shop -f seed.sql
-- Safe to re-run: it drops and rebuilds everything.
-- Tables get primary keys and foreign keys only. No other indexes, on purpose.

\set ON_ERROR_STOP on
\pset tuples_only on

DROP TABLE IF EXISTS orders, products, customers CASCADE;

-- Same seed = same data for every learner
SELECT setseed(0.42);

\echo 'Creating customers (100,000 rows)...'
CREATE TABLE customers (
  id          integer PRIMARY KEY,
  first_name  text        NOT NULL,
  last_name   text        NOT NULL,
  email       text        NOT NULL,
  city        text        NOT NULL,
  created_at  timestamptz NOT NULL
);

INSERT INTO customers (id, first_name, last_name, email, city, created_at)
SELECT
  i,
  f,
  l,
  f || '.' || l || i || '@example.com',
  city,
  ts
FROM (
  SELECT
    i,
    (ARRAY['Alice','Ben','Chloe','Dan','Ella','Finn','Grace','Harry','Isla','Jack',
           'Kate','Leo','Maya','Noah','Olivia','Priya','Sam','Tom','Zara','Yusuf'])[1 + floor(random() * 20)::int] AS f,
    (ARRAY['Smith','Jones','Taylor','Brown','Patel','Khan','Evans','Walker','Wright','Green',
           'Hall','Wood','Clarke','Hughes','Lewis','Ali','Scott','King','Baker','Moore'])[1 + floor(random() * 20)::int] AS l,
    (ARRAY['London','Manchester','Birmingham','Leeds','Glasgow','Bristol','Liverpool','Cardiff',
           'Sheffield','Edinburgh','Newcastle','Nottingham','Belfast','Brighton','Norwich'])[1 + floor(random() * 15)::int] AS city,
    timestamptz '2021-01-01' + random() * interval '1500 days' AS ts
  FROM generate_series(1, 100000) AS i
) s;

\echo 'Creating products (10,000 rows)...'
CREATE TABLE products (
  id        integer PRIMARY KEY,
  name      text          NOT NULL,
  category  text          NOT NULL,
  price     numeric(10,2) NOT NULL
);

INSERT INTO products (id, name, category, price)
SELECT
  i,
  (ARRAY['Classic','Deluxe','Mini','Pro','Eco','Ultra','Smart','Vintage'])[1 + floor(random() * 8)::int]
    || ' ' ||
  (ARRAY['Lamp','Mug','Chair','Kettle','Backpack','Speaker','Notebook','Jacket','Plant','Clock'])[1 + floor(random() * 10)::int]
    || ' ' || i,
  (ARRAY['Home','Kitchen','Garden','Tech','Fashion','Books','Sport','Toys'])[1 + floor(random() * 8)::int],
  round((2 + random() * 198)::numeric, 2)
FROM generate_series(1, 10000) AS i;

\echo 'Creating orders (2,000,000 rows). This is the slow one, give it a moment...'
CREATE TABLE orders (
  id           bigint        PRIMARY KEY,
  customer_id  integer       NOT NULL,
  product_id   integer       NOT NULL,
  status       text          NOT NULL,
  quantity     integer       NOT NULL,
  total        numeric(10,2) NOT NULL,
  created_at   timestamptz   NOT NULL
);

-- Status is deliberately skewed: ~85% delivered, ~10% shipped, ~4% pending, ~1% cancelled
INSERT INTO orders (id, customer_id, product_id, status, quantity, total, created_at)
SELECT
  i,
  1 + floor(random() * 100000)::int,
  1 + floor(random() * 10000)::int,
  CASE
    WHEN r < 0.85 THEN 'delivered'
    WHEN r < 0.95 THEN 'shipped'
    WHEN r < 0.99 THEN 'pending'
    ELSE 'cancelled'
  END,
  1 + floor(random() * 5)::int,
  round((5 + random() * 250)::numeric, 2),
  timestamptz '2023-01-01' + random() * interval '1000 days'
FROM (
  SELECT i, random() AS r FROM generate_series(1, 2000000) AS i
) s;

\echo 'Adding foreign keys...'
ALTER TABLE orders ADD CONSTRAINT orders_customer_fk FOREIGN KEY (customer_id) REFERENCES customers (id);
ALTER TABLE orders ADD CONSTRAINT orders_product_fk  FOREIGN KEY (product_id)  REFERENCES products (id);

\echo 'Vacuuming and gathering statistics...'
VACUUM ANALYZE customers, products, orders;

\echo 'Done. Row counts:'
\pset tuples_only off
SELECT 'customers' AS table_name, count(*) AS row_count FROM customers
UNION ALL SELECT 'products', count(*) FROM products
UNION ALL SELECT 'orders',   count(*) FROM orders;

