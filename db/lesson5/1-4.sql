/*
Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. Месяцы заданы в виде списка английских названий ('may', 'august')
*/

USE lesson5;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  birthday_at DATE
 );

INSERT INTO users (name, birthday_at)
VALUES
  ('Геннадий', '1990-10-05'),
  ('Наталья', '1984-11-12'),
  ('Александр', '1985-05-20'),
  ('Ирина', '1985-05-27'),
  ('Сергей', '1988-02-14'),
  ('Иван', '1998-01-12'),
  ('Петр', '1998-01-19'),
  ('Мария', '2006-08-29');
 
SELECT * FROM users;
SELECT name FROM users WHERE DATE_FORMAT(birthday_at, '%M') IN ('may', 'august')
