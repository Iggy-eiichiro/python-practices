SELECT 
    c.customer_id,
    c.first_name ||' '|| c.last_name AS customer_name,
    DATE '2022-09-01'- MAX(p.payment_date::DATE) AS recency_days,
    SUM(p.amount) AS total_monetary
FROM customer AS c
INNER JOIN payment AS p
    ON c.customer_id = p.customer_id
WHERE p.payment_date < '2022-09-01'
GROUP BY c.customer_id,c.first_name,c.last_name
ORDER BY total_monetary DESC;