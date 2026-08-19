SELECT 
    customer.customer_id,
    customer.first_name,
    customer.last_name,
    COUNT(rental.rental_id) as total_rentals 
FROM rental
INNER JOIN customer
    ON customer.customer_id = rental.customer_id
GROUP BY customer.customer_id, 
    customer.first_name,
    customer.last_name

HAVING COUNT(rental.rental_id) > 35
/*
HAVING total_rentals > 35
(from > join > where > group by > having > select > oreder by) that is the procedure
when turn come to "having", still not execute "select". that's why
*/
ORDER BY total_rentals DESC;