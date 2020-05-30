/*
по желанию) Пусть имеется таблица с календарным полем created_at. 
В ней размещены разряженые календарные записи за август 2018 года '2018-08-01', '2016-08-04', '2018-08-16' и 2018-08-17.
 Составьте запрос, который выводит полный список дат за август, выставляя в соседнем поле значение 1,
 если дата присутствует в исходном таблице и 0, если она отсутствует.
 */

USE shop;

DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (
	created_at DATE
);

INSERT INTO t1 VALUES
  ('2018-08-01'),
  ('2018-08-04'),
  ('2018-08-16'),
  ('2018-08-17');
  
 
CREATE TEMPORARY TABLE numbers (
	num SERIAL
);

INSERT INTO numbers VALUES (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ();
SELECT * FROM numbers;


SET @counter := -1;
SELECT 
	@curr_date := ADDDATE('2018-08-01', INTERVAL @counter := @counter + 1 DAY) AS month_day,
	IF(@curr_date IN (SELECT * FROM t1), 1, 0) AS exist
	FROM numbers;
