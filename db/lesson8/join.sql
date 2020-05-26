USE vk;

/*
 3. Подсчитать общее количество лайков десяти самым молодым пользователям (сколько лайков получили 10 самых молодых пользователей).
*/

SELECT SUM(total_likes) 
FROM  (
	SELECT COUNT(likes.id) AS total_likes
	FROM likes 
		JOIN target_types
			ON likes.target_type_id = target_types.id 
				AND target_types.name = 'users'
		RIGHT JOIN profiles
			ON likes.target_id = profiles.user_id
	GROUP BY profiles.user_id
	ORDER BY profiles.birthday DESC
	LIMIT 10
) AS likes_per_user;
 

-- Проверка
SELECT SUM(likes_total) FROM  
  (SELECT 
    (SELECT COUNT(*) FROM likes WHERE target_id = profiles.user_id AND target_type_id = 2) AS likes_total  
    FROM profiles 
    ORDER BY birthday 
    DESC LIMIT 10) AS user_likes
;
 
 
/*
4. Определить кто больше поставил лайков (всего) - мужчины или женщины?
*/

SELECT profiles.gender, COUNT(*) AS total_likes
FROM likes
	JOIN profiles
		ON likes.user_id = profiles.user_id
GROUP BY profiles.gender
ORDER BY total_likes DESC
LIMIT 1; 
 
-- Проверка
SELECT
	(SELECT gender FROM profiles WHERE user_id = likes.user_id) AS gender,
	COUNT(*) AS total_likes
    FROM likes
    GROUP BY gender
    ORDER BY total_likes DESC
    LIMIT 1;  
   
   
/*
5. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети
(критерии активности необходимо определить самостоятельно).
*/

SELECT 
	CONCAT(users.first_name, ' ', users.last_name) AS user,
	COUNT(messages.from_user_id) + COUNT(posts.user_id) + COUNT(likes.user_id) AS activity
FROM users
	LEFT JOIN messages 
		ON users.id = messages.from_user_id 
	LEFT JOIN posts 
		ON users.id = posts.user_id 
	LEFT JOIN likes 
		ON users.id = likes.user_id 
GROUP BY users.id
ORDER BY activity, users.last_name
LIMIT 10;

 
-- Проверка
SELECT 
  CONCAT(first_name, ' ', last_name) AS user, 
	(SELECT COUNT(*) FROM likes WHERE likes.user_id = users.id) + 
	(SELECT COUNT(*) FROM posts WHERE posts.user_id = users.id) + 
	(SELECT COUNT(*) FROM messages WHERE messages.from_user_id = users.id) AS activity 
	  FROM users
	  ORDER BY activity, last_name
	  LIMIT 10;

