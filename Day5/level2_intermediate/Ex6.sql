SELECT
    category.name as category_name,
    count(film_category) as total_films
    --COUNT(film_category.film_id) as total_films
    --count(film_category) is normally uncorrect
    -- because count() is a function that counts "values" or "rows" rather than "tables".
FROM category
INNER JOIN film_category

    ON category.category_id = film_category.category_id

GROUP BY category.category_id, category_name --colums not used in COUNT() must be include in GROUP BY
ORDER BY total_films DESC;