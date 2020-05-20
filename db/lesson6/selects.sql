USE vk;

/*
 3. Подсчитать общее количество лайков десяти самым молодым пользователям (сколько лайков получили 10 самых молодых пользователей).
*/
 
-- в TIMESTAMPDIFF используем DAY, так как пользователи могут быть одного года\месяца рождения
-- используем (SELECT * FROM(... LIMIT N) AS tmp), так как MySQL не дает напрямую использовать LIMIT во вложенных запросах

SELECT COUNT(*) AS likes_count FROM likes WHERE 
  target_type_id = (SELECT id FROM target_types WHERE name = 'users')
  AND
  target_id IN (SELECT * FROM (SELECT user_id FROM profiles ORDER BY TIMESTAMPDIFF(DAY, birthday, NOW()) LIMIT 10) AS tmp);

 
 
/*
4. Определить кто больше поставил лайков (всего) - мужчины или женщины?
*/

SELECT IF(
  (SELECT COUNT(*) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'm'))
  >=
  (SELECT COUNT(*) FROM likes WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'w')),
  'men',
  'women'
) AS most_likes_set;
 


/*
5. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети
(критерии активности необходимо определить самостоятельно).
*/

-- показатель активности: 20*<кол-во созданных сообщений> + 30*<кол-во созданныхпостов> +  50*<kол-во поставленных лайков>
-- где 20, 30, 50 - весовые коэффициенты

SELECT user_id, SUM(total) AS activity FROM (
	(SELECT from_user_id AS user_id, 20*COUNT(*) AS total FROM messages GROUP BY from_user_id)
	UNION
	(SELECT user_id, 30*COUNT(*) FROM posts GROUP BY user_id)
	UNION
	(SELECT user_id, 50*COUNT(*) FROM likes GROUP BY user_id)
) AS tmp GROUP BY user_id ORDER BY activity LIMIT 10;
