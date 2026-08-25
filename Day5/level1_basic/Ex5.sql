SELECT 
    CASE --kind of if in python
        WHEN rental_rate < 1.00 THEN 'Cheap'
        WHEN rental_rate <= 3.00 THEN 'Moderate'
        ELSE 'Expensive'
    END AS price_category,-- classify →　group → count

    COUNT(*) AS total_films-- count each group
FROM film
GROUP BY price_category
ORDER BY total_films DESC;