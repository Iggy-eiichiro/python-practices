WITH daily_revenue AS(
    SELECT
    payment_date::DATE AS pay_date,--payment_date::DATE. to be handled as date only
    SUM(amount) AS daily_amount
    FROM payment
    WHERE payment_date >= '2022-05-01'
        AND payment_date < '2022-06-01'
    GROUP BY payment_date::DATE
)
SELECT
    pay_date,
    daily_amount,
    SUM(daily_amount) OVER (-- over. specify range to use to calculate
        ORDER BY pay_date
    ) AS running_total
FROM daily_revenue
ORDER BY pay_date;