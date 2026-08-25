select count(*) as total_transactions, sum(amount) as total_revenue
from payment
where payment_date >= '2022-05-01'
and payment_date < '2022-06-01';
-- '2005-06-01'. it seems like string. but it is handed as "date".