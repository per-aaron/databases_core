-- file: migrations/003-add-genre-to-artists.sql
alter table artists add column country varchar(100);
