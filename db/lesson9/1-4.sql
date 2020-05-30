/*
(по желанию) Пусть имеется любая таблица с календарным полем created_at. 
Создайте запрос, который удаляет устаревшие записи из таблицы, оставляя только 5 самых свежих записей.
 */

USE shop;

DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (
	created_at DATE
);

INSERT INTO t1 VALUES
  ('1990-10-05'),
  ('1984-11-12'),
  ('1985-05-20'),
  ('1988-02-14'),
  ('1998-01-12'),
  ('1992-08-29'),
  ('2002-08-03'),
  ('2020-02-01');
  
 SELECT * FROM t1 ORDER BY created_at DESC;
 SELECT * FROM t1 ORDER BY created_at DESC LIMIT 5;
 SELECT @limit_date := created_at FROM t1 ORDER BY created_at DESC LIMIT 5;
 SELECT @limit_date;
 DELETE FROM t1 WHERE created_at < @limit_date;