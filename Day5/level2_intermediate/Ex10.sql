SELECT
    actor.actor_id,
    actor.first_name,
    actor.last_name
FROM actor

WHERE NOT EXISTS( --only person who do not have data that meet the condition will be selected
    SELECT 1 -- to check if there is a line that meets the condition.
    FROM film_actor 
    INNER JOIN film_category
        ON film_category.film_id = film_actor.film_id

    INNER JOIN category
        ON category.category_id = film_category.category_id
    WHERE actor.actor_id = film_actor.actor_id
        AND category.name = 'Action'


)

ORDER BY  actor.actor_id;