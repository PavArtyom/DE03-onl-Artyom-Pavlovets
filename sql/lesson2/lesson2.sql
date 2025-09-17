SELECT *
FROM actor a
WHERE a.last_name LIKE 'M%' AND EXTRACT(YEAR FROM a.last_update ) = 2017
ORDER BY a.last_name ASC, a.first_name ASC;

SELECT *
FROM staff s
WHERE s.active = TRUE  AND s.email LIKE '%.com'
ORDER BY s.last_name ASC, s.first_name ASC
LIMIT 10;

SELECT *
FROM payment p
WHERE p.amount BETWEEN 8.00 AND 10.00
ORDER BY p.payment_date::timestamp::date ASC, p.amount DESC
LIMIT 40;

