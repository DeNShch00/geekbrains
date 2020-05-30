/*
Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день",
 с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
 */

-- DELIMITER //
-- в настройках DBeaver нужно поставить разделитель // и убрать использование разделителя драйвера и использование пустух
-- строк в качестве разделителя

USE shop//

DROP FUNCTION hello//
CREATE FUNCTION hello() RETURNS VARCHAR(255) DETERMINISTIC 
BEGIN 
	DECLARE time_now TIME; 
	DECLARE hello_str VARCHAR(255) DEFAULT 'Добрый вечер'; 
	
	SET time_now := TIME(NOW());  
	
	IF (time_now >= TIME('00:00:00') AND time_now < TIME('06:00:00')) THEN 
		SET hello_str:= 'Доброй ночи'; 
	ELSEIF (time_now >= TIME('06:00:00') AND time_now < TIME('12:00:00')) THEN
		SET hello_str:= 'Доброе утро'; 
	ELSEIF (time_now >= TIME('12:00:00') AND time_now < TIME('18:00:00')) THEN
		SET hello_str:= 'Добрый день'; 
	END IF;
	
	RETURN hello_str; 
END//

SELECT hello()//
