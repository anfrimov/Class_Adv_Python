-- comments
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (id INTEGER PRIMARY KEY, name TEXT UNIQUE, age INTEGER);
INSERT INTO subjects (name, age) VALUES('luke', 37);