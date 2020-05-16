/*
����� � ������� users ���� created_at � updated_at ��������� ��������������. ��������� �� �������� ����� � ��������.
*/

CREATE DATABASE lesson5;
USE lesson5;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  birthday_at DATE,
  created_at DATETIME,
  updated_at DATETIME
 );

INSERT INTO users (name, birthday_at, created_at, updated_at)
VALUES
  ('��������', '1990-10-05', NULL, NULL),
  ('�������', '1984-11-12', NULL, NULL),
  ('���������', '1985-05-20', NULL, NULL),
  ('������', '1988-02-14', NULL, NULL),
  ('����', '1998-01-12', NULL, NULL),
  ('�����', '2006-08-29', NULL, NULL);
 
SELECT * FROM users;

UPDATE users SET created_at = NOW(), updated_at = NOW();
