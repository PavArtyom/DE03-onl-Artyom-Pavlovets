/* Выведите сводку по семейным фильмам (жанр Family), выпущенным начиная с 2007 года. 
   Для каждого года выпуска определите количество фильмов, среднюю, 
   минимальную и максимальную продолжительность. 
   Результат отсортируйте по году выпуска в порядке убывания. */

SELECT f.release_year, avg(f.length) AS avg_length, min(f.length) AS min_lenght, max(f.length ) AS max_length, 
count(f.film_id ) AS total_number_of_films
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON c.category_id = fc.category_id
WHERE f.release_year >= 2007 AND lower(c."name") = 'family'
GROUP BY f.release_year
ORDER BY f.release_year DESC;

/* Определите суммарную выручку и количество транзакций за 2007 год по каждой стране проживания клиентов. 
 Отсортируйте результат по выручке в порядке убывания и выведите только первые 10 стран. */

SELECT co.country, sum(p.amount) AS total_revenue, count(p.payment_id ) AS total_transact
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
JOIN address a ON a.address_id = c.address_id
JOIN city ct ON ct.city_id = a.city_id
JOIN country co ON co.country_id = ct.country_id
WHERE EXTRACT(YEAR FROM p.payment_date ) = 2017
GROUP BY co.country_id
ORDER BY total_revenue DESC
LIMIT 10;

/* Найдите пять категорий фильмов с наибольшим количеством фильмов. 
 Для каждой категории выведите количество фильмов и среднюю стоимость аренды. 
 Результат отсортируйте по числу фильмов в порядке убывания, а при равенстве — по названию категории. */

SELECT c."name", count(f.film_id ) AS total_number_of_films, avg(f.rental_rate ) AS avg_cost
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON c.category_id = fc.category_id
GROUP BY c.category_id
ORDER BY total_number_of_films DESC, c."name" 
LIMIT 5;





