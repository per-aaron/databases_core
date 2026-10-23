DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

INSERT INTO posts (title, content) VALUES ('Neurotoxin Inspection', 'An inspection is due to be carried out today');
INSERT INTO posts (title, content) VALUES ('Repulsion Gel', 'Those of you helping test the Repulsion Gel today, follow the blue line.');
INSERT INTO posts (title, content) VALUES ('Comedy', 'You know the old formula: comedy equals tragedy plus time. And you have been asleep for a while. So I guess it is actually pretty funny when you do the math.');
INSERT INTO posts (title, content) VALUES ('Potato Status', 'How are you holding up? Beacuse I am a potato [slow clap]. Oh, good. My slow clap processor made it into this thing.');