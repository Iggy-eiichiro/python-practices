SELECT 
    category.name AS category_name ,
    sum(payment.amount) AS total_revenue

FROM category
INNER JOIN film_category
    ON film_category.category_id = category.category_id
INNER JOIN inventory
    ON inventory.film_id = film_category.film_id
INNER JOIN rental
    ON rental.inventory_id = inventory.inventory_id
INNER JOIN payment
    ON payment.rental_id = rental.rental_id  
GROUP BY film_category.category_id, category.name
ORDER BY total_revenue DESC
LIMIT 5;--Limit the number of returned rows