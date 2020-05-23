/*
 * Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
 * Поля from, to и label содержат английские названия городов, поле name — русское. 
 * Выведите список рейсов flights с русскими названиями городов.
 */

USE lesson6;

CREATE TABLE flights (
	id SERIAL PRIMARY KEY,
	`from` VARCHAR(50),
	`to` VARCHAR(50)
);

INSERT INTO flights VALUES 
	(DEFAULT, 'moscow', 'omsk'),
	(DEFAULT, 'novgorod', 'kazan'),
	(DEFAULT, 'irkutsk', 'moscow'),
	(DEFAULT, 'omsk', 'irkutsk'),
	(DEFAULT, 'moscow', 'kazan');
	
CREATE TABLE cities (
	label VARCHAR(50),
	name VARCHAR(50),
	PRIMARY KEY (label, name)
);

INSERT INTO cities VALUES 
	('moscow', 'Москва'),
	('irkutsk', 'Иркутск'),
	('novgorod', 'Новгород'),
	('kazan', 'Казань'),
	('omsk', 'Омск');

SELECT * FROM flights;
SELECT * FROM cities;


SELECT 
	f.id,
	c_fr.name AS `from`,
	c_to.name AS `to`
FROM 
	flights AS f 
JOIN
	cities AS c_fr
JOIN 
	cities AS c_to 
ON 
	f.`from` = c_fr.label 
AND 
	f.`to` = c_to .label;

