-- Query Optimisation Lab: reset script
-- Drops every index you have created, keeping primary keys.
-- Usage: psql -d shop -f reset.sql

DO $$
DECLARE
  idx regclass;
BEGIN
  FOR idx IN
    SELECT i.indexrelid::regclass
    FROM pg_index i
    JOIN pg_class t ON t.oid = i.indrelid
    WHERE t.relname IN ('customers', 'products', 'orders')
      AND NOT EXISTS (
        SELECT 1 FROM pg_constraint c
        WHERE c.conindid = i.indexrelid AND c.contype IN ('p', 'u', 'x')
      )
  LOOP
    RAISE NOTICE 'Dropping index %', idx;
    EXECUTE 'DROP INDEX ' || idx;
  END LOOP;
END $$;

DROP TABLE IF EXISTS bench;
ANALYZE customers, products, orders;

