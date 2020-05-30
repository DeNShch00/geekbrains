/*
(по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел. 
Вызов функции FIBONACCI(10) должен возвращать число 55.
*/

-- DELIMITER //
-- в настройках DBeaver нужно поставить разделитель // и убрать использование разделителя драйвера и использование пустух
-- строк в качестве разделителя

USE shop//

DROP FUNCTION fibonacci//

CREATE FUNCTION fibonacci(num INT UNSIGNED) RETURNS INT UNSIGNED DETERMINISTIC 
BEGIN 
	DECLARE n1, n2, s INT UNSIGNED DEFAULT 1;
	
	IF num = 0 THEN
		RETURN 0;
	ELSEIF num = 1 THEN
		RETURN 1;
	END IF;
	
	WHILE num - 2 > 0 DO
		SET s := n1 + n2;
		SET n1 := n2;
		SET n2 := s;
		SET num := num - 1;
	END WHILE;	
	RETURN n2;
END//

SELECT fibonacci(4)//


