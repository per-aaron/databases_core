-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text,
  email text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email) VALUES ('benny1', 'ben1@mail.se');
INSERT INTO users (username, email) VALUES ('dallo', 'dalloway@mail.co.uk');
INSERT INTO users (username, email) VALUES ('emm', 'not3mm@mailmail.com');
INSERT INTO users (username, email) VALUES ('drac', 'nightowl@hotmail.com');
INSERT INTO users (username, email) VALUES ('wharty', 'lastone@mail.com');


DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views bigint,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content, views, user_id) VALUES ('ben is no.1', 'I am the best', 2, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('retraction', 'I might not be the best', 1, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Social media', 'What is with these posts', 22, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('Night benefits', 'Being awake at night is better', 5, 4);
INSERT INTO posts (title, content, views, user_id) VALUES ('Disappearance?', 'Why has emm not posted', 44, 5);
