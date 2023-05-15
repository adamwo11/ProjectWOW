CREATE DATABASE wow_char;
\c wow_char

-- CREATE TABLE char(
--     id SERIAL PRIMARY KEY,
--     name TEXT,
--     realm TEXT,
--     level integer NOT NULL,
--     gender TEXT,
--     classes TEXT,
--     race TEXT,
--     faction TEXT
-- );
DROP TABLE char;

CREATE TABLE char(
    id SERIAL PRIMARY KEY,
    name TEXT,
    realm TEXT,
    level integer NOT NULL
);
ALTER TABLE char ADD COLUMN img_url TEXT;
ALTER TABLE char ADD COLUMN gender TEXT;
ALTER TABLE char ADD COLUMN classes TEXT;
ALTER TABLE char ADD COLUMN race TEXT;
ALTER TABLE char ADD COLUMN faction TEXT;


SELECT * FROM char;


INSERT INTO char(name, realm, level, img_url, gender, classes, race, faction)
VALUES
('Plumbob', 'Frostmourne', '70','https://scontent.fadl3-1.fna.fbcdn.net/v/t1.15752-9/346154294_1871539633213919_1365357872945219264_n.png?stp=dst-png_p320x320&_nc_cat=100&ccb=1-7&_nc_sid=aee45a&_nc_ohc=DeK5_ZYC7EoAX9l_0yy&_nc_ht=scontent.fadl3-1.fna&oh=03_AdQ2aLKZttt-eAApCPPCXPr4DllpyE9deX7mbcLMiRbPTQ&oe=6489074A', 'Male', 'Hunter', 'Nightelf', 'Alliance'),
('Warwiz', 'Frostmourne', '56', 'https://scontent.fadl3-1.fna.fbcdn.net/v/t1.15752-9/346136188_162589140114245_5896913629695510506_n.png?stp=dst-png_s403x403&_nc_cat=104&ccb=1-7&_nc_sid=aee45a&_nc_ohc=6TZpTabnPxEAX8BAABv&_nc_ht=scontent.fadl3-1.fna&oh=03_AdRL2c4GtlHcRVBgdNRMWOhHqoe7F1PZQbh-ORact_EzEw&oe=6488FDCE', 'Male', 'Warlock', 'Orc', 'Horde');


INSERT INTO char(name, realm, level, img_url, gender, class, race, faction)
VALUES
('Kurth', 'Barthilas', '50', 'Female', 'Druid', 'Troll', 'Horde'),
('Aland', 'Barthilas', '58', 'Non-binary', 'Mage', 'Nightelf', 'Alliance');




-- INSERT INTO char(gender, class, race, faction)
-- VALUES
-- ('Male', 'Hunter', 'Nightelf', 'Alliance'),
-- ('Male', 'Warlock', 'Orc', 'Horde');
 CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  user_name TEXT,
  password_digest TEXT
);
DROP TABLE users;

CREATE TABLE likes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  char_id INTEGER
);