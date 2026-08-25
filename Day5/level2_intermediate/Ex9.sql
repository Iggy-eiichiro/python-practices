SELECT
    customer.first_name ||' '||customer.last_name AS customer_name,
    film.title,
    rental.rental_date
FROM rental
INNER JOIN  customer
    ON customer.customer_id = rental.customer_id  
INNER JOIN  inventory
    ON  rental.inventory_id = inventory.inventory_id
    --ON inventory.store_id = customer.store_id
INNER JOIN  film
    ON film.film_id = inventory.film_id
WHERE rental.return_date is NULL --Filter rows by conditions
    AND rental.rental_date < TIMESTAMP '2022-06-01' - INTERVAL '7 days'
ORDER BY rental.rental_date;
--TIMESTAMP is express the time
--INTERVAL. until deadline