/* Повысить цену аренды всех фильмов категории Comedy на 10 процентов, 
 используя обновление с подзапросом к таблицам film_category и category. */

UPDATE film
SET rental_rate = rental_rate * 1.10
WHERE film_id IN (SELECT film_id 
				  FROM film_category fc
				  JOIN category c ON fc.category_id = c.category_id
				  WHERE lower(c."name") = 'comedy' )
RETURNING *;

/* Удалить всех клиентов, которые находятся в статусе active = 0 и при этом не имеют ни одной записи в таблице rental. */

WITH del_cust AS (DELETE FROM customer c
WHERE c.active = 0 AND NOT EXISTS (
	SELECT 1
	FROM rental r
	WHERE c.customer_id = r.customer_id)
RETURNING *)

SELECT count(*) AS deleted_person
FROM del_cust;


/* Добавить новую запись в таблицу rental для любого фильма категории Action, 
 при этом арендатором должен быть клиент с наибольшим количеством аренд в истории, используя вставку с подзапросом. */

WITH
	calc_rents AS (
SELECT c.customer_id, count(r.customer_id) AS total_number
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id
ORDER BY total_number DESC),
	calc_inventory AS (
SELECT i.inventory_id
FROM inventory i
JOIN film_category fc ON i.film_id = fc.film_id
JOIN category c ON c.category_id = fc.category_id
WHERE lower(c.name) = 'action')




INSERT INTO rental (rental_date, inventory_id, customer_id, return_date, staff_id)
VALUES
(
    (now()),
    (SELECT inventory_id FROM calc_inventory LIMIT 1),
    (SELECT customer_id FROM calc_rents LIMIT 1),
    now(),
    1
)
RETURNING *;





	