/*
 Подсчитайте произведение чисел в столбце таблицы
*/

USE lesson5;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY
 );

INSERT INTO users VALUES (NULL), (NULL), (NULL), (NULL), (NULL)

SELECT * FROM users;
SELECT ROUND(EXP(SUM(LN(id)))) FROM users;

