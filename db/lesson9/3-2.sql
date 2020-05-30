/*
В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
При попытке присвоить полям NULL-значение необходимо отменить операцию.
*/

-- DELIMITER //
-- в настройках DBeaver нужно поставить разделитель // и убрать использование разделителя драйвера и использование пустух
-- строк в качестве разделителя

USE shop//

SELECT * FROM products//

DROP TRIGGER check_products_name_descr//
CREATE TRIGGER check_products_name_descr BEFORE INSERT on products
FOR EACH ROW
BEGIN
	IF (NEW.name IS NULL AND NEW.description IS NULL) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled: fileds name and description can\'t be NULL at same time';
	END IF;
END//

INSERT INTO products (name, description, price, catalog_id)
VALUES 
(NULL, NULL, 7890.00, 1)//