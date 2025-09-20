-- Найти все фильмы, продолжительность которых больше средней продолжительности всех фильмов в базе.

SELECT f.title, f.length
FROM film f
WHERE f.length > (SELECT avg(length) 
				  FROM film)
GROUP BY f.length, f.title 
ORDER BY f.length desc;

WITH calc_avg_duration AS (SELECT AVG(length) AS avg_len 
				   		   FROM film )

SELECT title, length
FROM film, calc_avg_duration
WHERE length > calc_avg_duration.avg_len
ORDER BY length;


-- Найти сотрудников (staff), которые работают в том же магазине, что и клиент с фамилией SMITH.

SELECT s.staff_id, s.first_name, s.last_name 
FROM staff s 
WHERE store_id = (SELECT c.store_id 
				  FROM customer c 
				  WHERE lower(c.last_name)  = 'smith');


SELECT s.staff_id, s.first_name, s.last_name
FROM customer c
JOIN staff s ON s.store_id  = c.store_id 
WHERE lower(c.last_name) = 'smith';

-- Найти клиентов, которые заплатили больше, чем средняя сумма платежа по всей базе.

SELECT c.first_name, c.last_name, p.amount, (SELECT avg(amount) AS avg_payment FROM payment)
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
WHERE p.amount > ( SELECT  avg(amount) 
				   FROM payment )
GROUP BY c.first_name, c.last_name, p.amount
ORDER BY p.amount ASC;



WITH calc_avg_paym AS (SELECT AVG(amount) AS avg_amount 
				   FROM payment )

SELECT c.customer_id, c.first_name, c.last_name,  p.amount, calc_avg_paym.avg_amount
FROM calc_avg_paym, customer c
JOIN payment p ON c.customer_id = p.customer_id 
WHERE p.amount > calc_avg_paym.avg_amount
ORDER BY p.amount ASC;






