USE vk;

-- таблица постов
CREATE TABLE posts (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  user_id INT UNSIGNED NOT NULL, -- автор поста
  content TEXT NOT NULL, -- содержание поста в виде HTML-документа
  views INT UNSIGNED NOT NULL, -- количество просмотров
  status_id INT UNSIGNED NOT NULL, -- статус поста
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- создан
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- отредактирован
);

-- таблица статусов поста
CREATE TABLE posts_statuses (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
   status VARCHAR(50) -- активный\в архиве\удален
 );

-- медиа прикрепленные к посту
CREATE TABLE posts_media (
   post_id INT UNSIGNED NOT NULL,
   media_id INT UNSIGNED NOT NULL,
   number INT UNSIGNED, -- порядок следования медиа в списке медиа прикрепленного к посту
   PRIMARY KEY (post_id, media_id)
 );

-- таблица комментариев под постами
-- поддерживает логику ответа на комментарий
CREATE TABLE posts_comments (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  post_id INT UNSIGNED NOT NULL, -- внешний ключ на posts
  answer_on_id INT UNSIGNED NOT NULL, -- id комментария из данной таблицы, на который идет ответ; значение 0 - комментарий на сам пост
  content TEXT NOT NULL, -- содержание комментария
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- создан
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- отредактирован
);

-- лайки\дизлайки постов
CREATE TABLE posts_likes (
  post_id INT UNSIGNED NOT NULL,
  user_id INT UNSIGNED NOT NULL, -- пользователь ставящий лайк\дизлайк
  likes BOOLEAN NOT NULL, -- TURE - лайк, FALSE - дизлайк
  PRIMARY KEY (post_id, user_id)
);

-- лайки\дизлайки комментариев постов
CREATE TABLE posts_comments_likes (
  post_comment_id INT UNSIGNED NOT NULL,
  user_id INT UNSIGNED NOT NULL, -- пользователь ставящий лайк\дизлайк
  likes BOOLEAN NOT NULL, -- TURE - лайк, FALSE - дизлайк
  PRIMARY KEY (post_comment_id, user_id)
);

-- таблица тегов
CREATE TABLE tags (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  value VARCHAR(50) -- тег, например "Природа"
);

-- таблица сопоставления тегов постам
CREATE TABLE posts_tags (
  post_id INT UNSIGNED NOT NULL,
  tag_id INT UNSIGNED NOT NULL,
  PRIMARY KEY (post_id, tag_id)
 );



