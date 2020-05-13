USE vk;

------------------------------------
-- ��������� ����� ������� � �������
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
-- ������ �������� ������ ����� �����������������
-------------------------------------------------

-- ������ ������� �� ������������ ������� ������ ���� user_id, ��� ��� ��� ��� ������� � ������� filldb 

-- �������� � ������� ��������� �����
UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE created_at > updated_at;
UPDATE media SET updated_at = CURRENT_TIMESTAMP WHERE created_at > updated_at;
UPDATE friendship SET confirmed_at = CURRENT_TIMESTAMP WHERE requested_at > confirmed_at;

-- ��������� ������ �� ����
UPDATE profiles SET photo_id = FLOOR(1 + RAND() * 100);
  
-- ����������� �����������
UPDATE profiles SET is_private = TRUE WHERE user_id > FLOOR(1 + RAND() * 100);  

-- ������� ��� ����
TRUNCATE media_types;

-- ��������� ������ ����
INSERT INTO media_types (name) VALUES
  ('photo'),
  ('video'),
  ('audio')
;

-- ��������� ��� �����
UPDATE media SET media_type_id = FLOOR(1 + RAND() * 3);

-- ������ ��������� ������� �������� �����������
CREATE TEMPORARY TABLE extensions (name VARCHAR(10));

-- ��������� ����������
INSERT INTO extensions VALUES ('jpeg'), ('avi'), ('mpeg'), ('png');

-- ��������� ������ �� ����
UPDATE media SET filename = CONCAT('https://dropbox/vk/',
  filename,
  '.',
  (SELECT name FROM extensions ORDER BY RAND() LIMIT 1)
);

-- ��������� ������ ������
UPDATE media SET size = FLOOR(10000 + (RAND() * 1000000)) WHERE size < 1000;

-- ��������� ����������
UPDATE media SET metadata = CONCAT('{"owner":"', 
  (SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = user_id),
  '"}');  

-- ������� �������
TRUNCATE friendship_statuses;

-- ��������� �������� �������� ������
INSERT INTO friendship_statuses (name) VALUES
  ('Requested'),
  ('Confirmed'),
  ('Rejected');
 
-- ��������� ������ �� ������ 
UPDATE friendship SET status_id = FLOOR(1 + RAND() * 3); 


