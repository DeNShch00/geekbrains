/*
Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.
*/

/*
 Подсчитайте средний возраст пользователей в таблице users
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
SELECT 
  DATE_FORMAT(DATE(CONCAT_WS('-', YEAR(NOW()), MONTH(birthday_at), DAY(birthday_at))), '%W') AS day,
  COUNT(*) AS total 
 FROM users
GROUP BY day
ORDER BY total;
