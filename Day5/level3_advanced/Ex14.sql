SELECT 
    a1.first_name || ' ' || a1.last_name AS actor_1,
    a2.first_name || ' ' || a2.last_name AS actor_2,
    COUNT(*) AS shared_films
FROM film_actor AS fa1
INNER JOIN film_actor AS fa2
    ON fa1.film_id = fa2.film_id
    AND fa1.actor_id < fa2.actor_id -- not to count same pair
INNER JOIN actor AS a1
    ON fa1.actor_id = a1.actor_id
INNER JOIN actor AS a2
    ON fa2.actor_id = a2.actor_id
GROUP BY
    a1.actor_id,
    a1.first_name,
    a1.last_name,
    a2.actor_id,
    a2.first_name,
    a2.last_name
    -- why actor is put in GROUP BY? because if shows up EIICHIRO, EIICHIRO. can not recognize
HAVING COUNT(*) >= 3
ORDER BY shared_films;