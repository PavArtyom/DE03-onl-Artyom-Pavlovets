/* Создайте таблицу с 500 000–1 000 000 строк (например, заказы клиентов). 
 Выполните поиск и сортировку данных без индексов, затем добавьте индекс по ключевому полю (например, status или order_date). 
 Сравните время выполнения запросов до и после добавления индекса и сделайте вывод о влиянии индексации на производительность. */

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    status VARCHAR(20),
    order_date DATE,
    amount NUMERIC(10,2)
);


INSERT INTO orders (customer_id, status, order_date, amount)
SELECT
    (random() * 100000)::INT,                                
    (ARRAY['new','processing','shipped','delivered'])[ceil(random()*4)],
    date '2020-01-01' + (random() * 1000)::INT,             
    (random() * 1000)::NUMERIC(10,2)                         
FROM generate_series(1, 1000000); 

EXPLAIN ANALYZE
SELECT * 
FROM orders 
WHERE status = 'shipped'; --seq scan 101.938 ms 




EXPLAIN ANALYZE --sort, seq scan 113.407 ms 
SELECT * 
FROM orders 
WHERE order_date BETWEEN '2021-01-01' AND '2022-01-01';


CREATE INDEX idx_orders_status ON orders(status);

CREATE INDEX idx_orders_date ON orders(order_date);


EXPLAIN ANALYZE --index scan 73.636
SELECT * 
FROM orders 
WHERE status = 'shipped';


EXPLAIN ANALYZE  --index scan 80.161 
SELECT * 
FROM orders o
WHERE o.order_date BETWEEN '2021-01-01' AND '2022-01-01';


/* Для базы данных с таблицами Пользователи, Продукты и Заказы предложите оптимальные типы индексов под задачи: поиск заказов конкретного пользователя,
 определение самых популярных продуктов, анализ динамики продаж по месяцам. Обоснуйте выбор индексов (B-Tree, BRIN, GIN) 
 и продемонстрируйте их работу на тестовых данных. */

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT
);

CREATE TABLE orders1 (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    product_id INT REFERENCES products(product_id),
    order_date DATE
);

INSERT INTO users(name)
SELECT 'User ' || g
FROM generate_series(1,100000) g;

INSERT INTO products(name, description)
SELECT 'Product ' || g, 'Описание продукта ' || g
FROM generate_series(1,50000) g;

INSERT INTO orders1(user_id, product_id, order_date)
SELECT (random()*99)::int + 1,
       (random()*49)::int + 1,
       date '2020-01-01' + (random()*1460)::int
FROM generate_series(1,500000);

EXPLAIN ANALYZE
SELECT * 
FROM orders1 
WHERE user_id = 520; --seq scan 34.687 ms --index cond:0.092 ms - b-tree эффективен для поиска заказов конкретн. польз.

CREATE INDEX idx_orders1_user ON orders1(user_id);

EXPLAIN ANALYZE
SELECT product_id, COUNT(*) AS cnt
FROM orders1
GROUP BY product_id
ORDER BY cnt DESC; --seq scan 55.703 ms b-tree будет эффективнее при группировке и сортировке.

CREATE INDEX idx_orders1_product ON orders1(product_id);

EXPLAIN ANALYZE
SELECT EXTRACT(MONTH FROM order_date) AS month, COUNT(*) AS total_orders
FROM orders1
GROUP BY month
ORDER BY total_orders; --seq scan 72.679 ms, BRIN более эффективен для временных рядов.

CREATE INDEX idx_orders1_date_brin ON orders1 USING BRIN(order_date);

CREATE INDEX idx_orders1_extract_date_brin ON orders1 (EXTRACT (MONTH FROM order_date));







