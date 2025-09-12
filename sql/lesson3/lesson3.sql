/* Вывести названия фильмов жанра Action, которые сняты на английском языке. 
 Отсортировать по году выпуска (от новых к старым) и вывести первые 20 строк. */

SELECT
	f.title
FROM 
	film f
JOIN 
	language l ON f.language_id = l.language_id
JOIN 
	film_category fc ON fc.film_id = f.film_id
JOIN
	category c ON c.category_id = fc.category_id
WHERE
	c.name = 'Action' AND l.name = 'English'
ORDER BY
	f.release_year DESC
LIMIT 
	20;

/* Показать клиентов и города магазинов, к которым они относятся. 
 Вывести только тех клиентов, у которых город начинается на букву A. 
 Отсортировать по фамилии клиента, ограничить результат 25 строками. */

SELECT
	c.first_name, c.last_name, c3.city 
FROM
	customer c
JOIN
	store s ON s.store_id = c.store_id
JOIN
	address a ON c.address_id = a.address_id
JOIN
	city c2 ON c2.city_id = a.city_id
JOIN
	address a2 ON a2.address_id = s.address_id
JOIN
	city c3 ON c3.city_id = a2.city_id
WHERE
	upper(c2.city) LIKE 'A%'
ORDER BY
	c.last_name ASC
LIMIT
	25;
	

/* Показать список клиентов, фильмов и сумм платежей, где сумма оплаты больше 5. 
 Отсортировать по сумме (по убыванию), затем по дате платежа (по убыванию). 
 Ограничить результат 30 строками. */

SELECT
	c.first_name, c.last_name, f.title, p.amount
FROM
	customer c
JOIN
	rental r ON c.customer_id = r.customer_id
JOIN
	inventory i ON r.inventory_id = i.inventory_id
JOIN
	film f ON i.film_id = f.film_id
JOIN
	payment p ON p.rental_id = r.rental_id
WHERE
	p.amount > 5
ORDER BY 
	p.amount DESC, p.payment_date DESC
LIMIT 
	30;


--Вывести все фильмы, в которых снимался актёр или актриса с фамилией MONROE. Отсортировать по названию фильма.

SELECT
	f.title
FROM
	film f
JOIN
	film_actor fa ON fa.film_id = f.film_id
JOIN
	actor a ON a.actor_id = fa.actor_id
WHERE
	upper(a.last_name) = 'MONROE'
ORDER BY 
	f.title ASC;

/* Показать список клиентов и фильмов, которые они арендовали и ещё не вернули (return_date IS NULL). 
 Отсортировать по дате аренды (от новых к старым) и вывести 20 строк. */

SELECT
	c.first_name, c.last_name, f.title
FROM
	customer c
JOIN
	rental r ON r.customer_id = c.customer_id
JOIN
	inventory i ON i.inventory_id = r.inventory_id
JOIN
	film f ON f.film_id = i.film_id
WHERE
	r.return_date IS NULL
ORDER BY 
	r.rental_date DESC
LIMIT 
	20;






	

