/* Операции обновления с проверкой условий
Создайте транзакцию для таблицы accounts, которая уменьшает баланс на 1000 для
всех счетов, чей баланс превышает 5000. Если операция прошла успешно,
зафиксируйте изменения. В случае ошибки откатите транзакцию. */

CREATE TABLE IF NOT EXISTS public.accounts (
	acc_id serial PRIMARY KEY,
	full_name varchar(50) NOT NULL,
	balance decimal (10,2)
);

INSERT INTO accounts (full_name, balance)
	VALUES ('Artyom Ivanov', 6000.51),
		   ('Denis Denisov', 1100.12),
		   ('Kirill Kirillov', 8512.10 ),
		   ('Vasya Vasyliev', 2500.13)
		   
BEGIN;
UPDATE accounts
SET balance = balance - 1000
WHERE balance > 5000;

SELECT *
FROM accounts;

COMMIT;
ROLLBACK;
		   
/* Последовательные вставки с проверкой ошибок
Напишите транзакцию для таблицы inventory, которая добавляет новый товар и
сразу же обновляет количество на складе. Если хотя бы одна из операций завершится с
ошибкой, отмените транзакцию. */

CREATE TABLE IF NOT EXISTS inventory (
	id serial PRIMARY KEY,
	product_name varchar(50) NOT NULL,
	quantity int NOT NULL
);

CREATE TABLE IF NOT EXISTS warehouse (
	id serial PRIMARY KEY,
	product_id int,
	stock int NOT NULL,
	CONSTRAINT fk_inv_wh
	FOREIGN KEY (product_id)
	REFERENCES inventory(id)
);


BEGIN;

WITH add_new_item AS (
    INSERT INTO inventory (product_name, quantity)
    VALUES ('shoes', 20)
  	RETURNING id, quantity
)

INSERT INTO warehouse (product_id, stock)
SELECT id, quantity FROM add_new_item;
   


COMMIT;
ROLLBACK;


/* Создание резервной копии и удаление данных
Создайте транзакцию, которая сначала создает резервную копию таблицы users в
users_backup, а затем удаляет все записи из users, чей статус равен 'inactive'.
Если операция удаления не удалась, откатите транзакцию. */

CREATE TABLE IF NOT EXISTS public.users ( 
	user_id SERIAL PRIMARY KEY, 
	full_name VARCHAR(50) NOT NULL, 
	status VARCHAR(50)
);

INSERT INTO users (full_name, status)
VALUES ('Alex King', 'active'),
	   ('Lebron James', 'inactive'),
	   ('James Jamerson', 'inactive'),
	   ('Michel Kante', 'active');

BEGIN;
CREATE TABLE IF NOT EXISTS users_backup AS TABLE users

DELETE FROM users
WHERE status = 'inactive';

SELECT *
FROM users;

SELECT *
FROM users_backup;

COMMIT;
ROLLBACK;
