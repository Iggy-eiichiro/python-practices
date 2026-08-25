WITH customer_spending AS (
    SELECT
        c.customer_id,  
        c.first_name ||' '|| c.last_name AS name,
        SUM(p.amount) AS total_spent
    FROM customer AS c
    INNER JOIN payment as p
        ON p.customer_id = c.customer_id
    
    GROUP BY  c.customer_id, c.first_name, c.last_name
--[COUNT/SUM/AVG /MAX/MIN] > use GROUP BY
),
overall_average AS (
    SELECT AVG(cs.total_spent) AS overall_avg
    FROM customer_spending AS cs
)
SELECT
    cs.customer_id,
    cs.name,
    cs.total_spent
FROM customer_spending AS cs
CROSS JOIN overall_average AS oa -- no correspondence, combine all. no ON
WHERE cs.total_spent > oa.overall_avg
ORDER BY cs.total_spent DESC;