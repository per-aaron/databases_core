
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  author text,
  content text,
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

INSERT INTO comments (author, content, post_id) VALUES ('Wheatley', 'begin!', 1);
INSERT INTO comments (author, content, post_id) VALUES ('definitelyNotWheatley', 'Hello Guv. Here are my credentials, shut yourself down', 1);
INSERT INTO comments (author, content, post_id) VALUES ('definitelyNotWheatley', 'I am totally legit, from the board of international, uh, observers, from the UAE', 1);
INSERT INTO comments (author, content, post_id) VALUES ('Chell', '...', 1);
INSERT INTO comments (author, content, post_id) VALUES ('Lab tech 1', 'Some advice, do not get covered in Repulsion Gel', 2);
INSERT INTO comments (author, content, post_id) VALUES ('Lab tech 2', 'We have not entirely nailed down what element it is yet', 2);
INSERT INTO comments (author, content, post_id) VALUES ('Lab tech 3', 'I will tell you this, it is a lively one, and it does not like the human skeleton', 2);
