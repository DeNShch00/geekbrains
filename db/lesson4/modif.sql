USE vk;

------------------------------------
-- Добавляем новые столбцы и таблицы
------------------------------------

ALTER TABLE profiles DROP COLUMN created_at;

ALTER TABLE profiles ADD photo_id INT UNSIGNED AFTER user_id;

CREATE TABLE user_statuses (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL UNIQUE
);

INSERT user_statuses (id, name)
VALUES
  (1, 'active'),
  (2, 'blocked'),
  (3, 'deleted');

ALTER TABLE users ADD status_id INT UNSIGNED NOT NULL DEFAULT 1 AFTER phone;

ALTER TABLE profiles ADD is_private BOOLEAN DEFAULT FALSE AFTER country;


-------------------------------------------------
-- Делаем тестовые данные более репрезентативными
-------------------------------------------------

-- убраны команды по рандомизации внешних ключей типа user_id, так как это уже сделано с помощью filldb 

-- Приводим в порядок временные метки
UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE created_at > updated_at;
UPDATE media SET updated_at = CURRENT_TIMESTAMP WHERE created_at > updated_at;
UPDATE friendship SET confirmed_at = CURRENT_TIMESTAMP WHERE requested_at > confirmed_at;

-- Добавляем ссылки на фото
UPDATE profiles SET photo_id = FLOOR(1 + RAND() * 100);
  
-- Проставляем приватность
UPDATE profiles SET is_private = TRUE WHERE user_id > FLOOR(1 + RAND() * 100);  

-- Удаляем все типы
TRUNCATE media_types;

-- Добавляем нужные типы
INSERT INTO media_types (name) VALUES
  ('photo'),
  ('video'),
  ('audio')
;

-- Обновляем тип медиа
UPDATE media SET media_type_id = FLOOR(1 + RAND() * 3);

-- Создаём временную таблицу форматов медиафайлов
CREATE TEMPORARY TABLE extensions (name VARCHAR(10));

-- Заполняем значениями
INSERT INTO extensions VALUES ('jpeg'), ('avi'), ('mpeg'), ('png');

-- Обновляем ссылку на файл
UPDATE media SET filename = CONCAT('https://dropbox/vk/',
  filename,
  '.',
  (SELECT name FROM extensions ORDER BY RAND() LIMIT 1)
);

-- Обновляем размер файлов
UPDATE media SET size = FLOOR(10000 + (RAND() * 1000000)) WHERE size < 1000;

-- Заполняем метаданные
UPDATE media SET metadata = CONCAT('{"owner":"', 
  (SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = user_id),
  '"}');  

-- Очищаем таблицу
TRUNCATE friendship_statuses;

-- Вставляем значения статусов дружбы
INSERT INTO friendship_statuses (name) VALUES
  ('Requested'),
  ('Confirmed'),
  ('Rejected');
 
-- Обновляем ссылки на статус 
UPDATE friendship SET status_id = FLOOR(1 + RAND() * 3); 


