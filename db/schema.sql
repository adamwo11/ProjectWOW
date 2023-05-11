CREATE DATABASE wow_char;
\c wow_char

CREATE TABLE char(
    id SERIAL PRIMARY KEY,
    name TEXT,
    realm TEXT,
    level integer NOT NULL,
    gender TEXT,
    class TEXT,
    race TEXT,
    faction TEXT
);

 CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  email TEXT,
  password_digest TEXT
);