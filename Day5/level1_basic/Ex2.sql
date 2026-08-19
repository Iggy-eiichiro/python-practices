SELECT rating , count(*) as total_films, round(avg(rental_rate),2) as avg_rental_rate
/*
count(*) as total_films, Do count them and make the name as a number. the numbers get total_films
when i use count, use () cauz it is various
round(avg(rental_rate),2) as avg_rental_rate. round make definition decimal where to put ".".
*/
from film 
group by rating 
order by  total_films desc;