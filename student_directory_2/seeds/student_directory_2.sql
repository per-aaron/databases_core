DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date DATE
);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
-- The foreign key name is always {other_table_singular}_id
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('Leander', '1930-09-08');
INSERT INTO cohorts (name, starting_date) VALUES ('Orion', '1931-09-26');
INSERT INTO cohorts (name, starting_date) VALUES ('Neptune', '1932-01-31');
INSERT INTO cohorts (name, starting_date) VALUES ('Ajax', '1933-03-01');
INSERT INTO cohorts (name, starting_date) VALUES ('Apollo', '1934-10-09');

INSERT INTO students (name, cohort_id) VALUES ('Jervis', 1);
INSERT INTO students (name, cohort_id) VALUES ('Jackal', 1);
INSERT INTO students (name, cohort_id) VALUES ('Juno', 1);
INSERT INTO students (name, cohort_id) VALUES ('Javelin', 2);
INSERT INTO students (name, cohort_id) VALUES ('Jupiter', 2);
INSERT INTO students (name, cohort_id) VALUES ('Kelly', 2);
INSERT INTO students (name, cohort_id) VALUES ('Kandahar', 3);
INSERT INTO students (name, cohort_id) VALUES ('Kelvin', 3);
INSERT INTO students (name, cohort_id) VALUES ('Khartoum', 3);
INSERT INTO students (name, cohort_id) VALUES ('Kipling', 4);
INSERT INTO students (name, cohort_id) VALUES ('Napier', 4);
INSERT INTO students (name, cohort_id) VALUES ('Nestor', 4);
INSERT INTO students (name, cohort_id) VALUES ('Norman', 5);
INSERT INTO students (name, cohort_id) VALUES ('Nerissa', 5);