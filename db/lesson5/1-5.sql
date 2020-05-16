/*
 * Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN.
*/

USE lesson5;

CREATE TABLE catalogs (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

INSERT INTO catalogs VALUES
  (NULL, 'Процессоры'),
  (NULL, 'Материнские платы'),
  (NULL, 'Видеокарты'),
  (NULL, 'Жесткие диски'),
  (NULL, 'Оперативная память');
  
SELECT * FROM catalogs;
SELECT id, name, FIELD(id, 5, 1, 2) AS pos FROM catalogs WHERE id IN(5, 1, 2);
SELECT * FROM catalogs WHERE id IN(5, 1, 2) ORDER BY FIELD(id, 5, 1, 2);