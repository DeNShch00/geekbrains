/*
 ����������� ������� ������� ������������� � ������� users
*/

USE lesson5;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  birthday_at DATE
 );

INSERT INTO users (name, birthday_at)
VALUES
  ('��������', '1990-10-05'),
  ('�������', '1984-11-12'),
  ('���������', '1985-05-20'),
  ('������', '1988-02-14'),
  ('����', '1998-01-12'),
  ('�����', '2006-08-29');
 
SELECT * FROM users;
SELECT TIMESTAMPDIFF(YEAR, birthday_at, NOW()) AS age FROM users;
SELECT AVG(TIMESTAMPDIFF(YEAR, birthday_at, NOW())) AS age FROM users;