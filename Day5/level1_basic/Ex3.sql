select title, replacement_cost, rating
from film
where title like '%LOVE%'
/*
like 'love'. accuracy same with love
like 'love%'. start with love
like '%love'. end with love
like '%love%'. include love
*/
and replacement_cost between 10 and 20
and rating in ('G','PG') ;
/*
match  G or PG.
in SQL if characters are strings, need ''.
*/