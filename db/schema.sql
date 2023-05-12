CREATE DATABASE wow_char;
\c wow_char

CREATE TABLE char(
    id SERIAL PRIMARY KEY,
    name TEXT,
    realm TEXT,
    level integer NOT NULL,
    gender TEXT,
    classes TEXT,
    race TEXT,
    faction TEXT
);
DROP TABLE char;

 CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  user_name TEXT,
  password_digest TEXT
);
DROP TABLE users;