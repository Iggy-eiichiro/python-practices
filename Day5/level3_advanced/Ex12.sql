WITH film_revenue AS (
    SELECT
        c.name AS category_name,
        f.film_id,
        f.title,
        SUM(p.amount) AS revenue
    FROM category AS c
    INNER JOIN film_category AS fc
        ON c.category_id = fc.category_id
    INNER JOIN film AS f
        ON fc.film_id = f.film_id
    INNER JOIN inventory AS i
        ON f.film_id = i.film_id
    INNER JOIN rental r
        ON i.inventory_id = r.inventory_id
    INNER JOIN payment AS p
        ON r.rental_id = p.rental_id
    GROUP BY c.category_id, c.name, f.film_id, f.title
),
ranked_film AS(
    SELECT
        fr.category_name,
        fr.title,
        fr.revenue,
        DENSE_RANK() OVER(
            PARTITION BY fr.category_name 
            ORDER BY fr.revenue DESC) AS rank_in_category
    FROM film_revenue AS fr
)
SELECT
    rf.category_name,
    rf.title,
    rf.revenue,
    rf.rank_in_category
FROM ranked_film AS rf
WHERE rf.rank_in_category <= 2
ORDER BY rf.rank_in_category;