USE vk;

-- ������� ������
CREATE TABLE posts (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  user_id INT UNSIGNED NOT NULL, -- ����� �����
  content TEXT NOT NULL, -- ���������� ����� � ���� HTML-���������
  views INT UNSIGNED NOT NULL, -- ���������� ����������
  status_id INT UNSIGNED NOT NULL, -- ������ �����
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- ������
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- ��������������
);

-- ������� �������� �����
CREATE TABLE posts_statuses (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
   status VARCHAR(50) -- ��������\� ������\������
 );

-- ����� ������������� � �����
CREATE TABLE posts_media (
   post_id INT UNSIGNED NOT NULL,
   media_id INT UNSIGNED NOT NULL,
   number INT UNSIGNED, -- ������� ���������� ����� � ������ ����� �������������� � �����
   PRIMARY KEY (post_id, media_id)
 );

-- ������� ������������ ��� �������
-- ������������ ������ ������ �� �����������
CREATE TABLE posts_comments (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  post_id INT UNSIGNED NOT NULL, -- ������� ���� �� posts
  answer_on_id INT UNSIGNED NOT NULL, -- id ����������� �� ������ �������, �� ������� ���� �����; �������� 0 - ����������� �� ��� ����
  content TEXT NOT NULL, -- ���������� �����������
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- ������
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- ��������������
);

-- �����\�������� ������
CREATE TABLE posts_likes (
  post_id INT UNSIGNED NOT NULL,
  user_id INT UNSIGNED NOT NULL, -- ������������ �������� ����\�������
  likes BOOLEAN NOT NULL, -- TURE - ����, FALSE - �������
  PRIMARY KEY (post_id, user_id)
);

-- �����\�������� ������������ ������
CREATE TABLE posts_comments_likes (
  post_comment_id INT UNSIGNED NOT NULL,
  user_id INT UNSIGNED NOT NULL, -- ������������ �������� ����\�������
  likes BOOLEAN NOT NULL, -- TURE - ����, FALSE - �������
  PRIMARY KEY (post_comment_id, user_id)
);

-- ������� �����
CREATE TABLE tags (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  value VARCHAR(50) -- ���, �������� "�������"
);

-- ������� ������������� ����� ������
CREATE TABLE posts_tags (
  post_id INT UNSIGNED NOT NULL,
  tag_id INT UNSIGNED NOT NULL,
  PRIMARY KEY (post_id, tag_id)
 );



