/* 1. Составные ключи и связи в цепочке таблиц
Создайте три таблицы:
departments(dept_id, dept_name) — первичный ключ dept_id.
employees(emp_id, dept_id, full_name) — первичный ключ emp_id, внешний ключ dept_id ссылается на departments.
projects(project_id, dept_id, project_name) — первичный ключ project_id, внешний ключ dept_id ссылается на departments.
Теперь создайте таблицу employee_projects, где хранится назначение сотрудников на проекты.
В ней должен быть составной первичный ключ (emp_id, project_id) и два внешних ключа, ссылающихся на employees(emp_id) и projects(project_id).
Вставьте корректные данные и попробуйте вставить запись с несуществующим emp_id или project_id. */

CREATE TABLE IF NOT EXISTS public.departments (
	dept_id serial PRIMARY KEY,
	dept_name varchar(50) NOT NULL 
);

CREATE TABLE IF NOT EXISTS public.employees (
	emp_id serial PRIMARY KEY,
	full_name varchar(50) NOT NULL,
	dept_id int,
	CONSTRAINT fk_dep_emp
	FOREIGN KEY (dept_id)
	REFERENCES departments (dept_id)
	);

CREATE TABLE IF NOT EXISTS public.projects (
	project_id serial PRIMARY KEY,
	project_name varchar(50) NOT NULL,
	dept_id int,
	CONSTRAINT fk_dep_proj
	FOREIGN KEY (dept_id)
	REFERENCES departments (dept_id)
	);

CREATE TABLE IF NOT EXISTS public.employee_projects (
	emp_id int NOT NULL,
	project_id int NOT NULL,
	CONSTRAINT pk_emp_proj
	PRIMARY KEY (emp_id, project_id),
	CONSTRAINT fk_emp
	FOREIGN KEY (emp_id)
	REFERENCES employees (emp_id),
	CONSTRAINT fk_proj
	FOREIGN KEY (project_id)
	REFERENCES projects (project_id)
	);

INSERT INTO departments (dept_name)
VALUES 
	('finance'),
	('technology'),
	('marketing'),
	('innovation'),
	('sales');

INSERT INTO employees(full_name, dept_id)
VALUES 
	('Larry Fink', (SELECT dept_id FROM departments WHERE lower(dept_name) = 'finance')),
	('William Gates', (SELECT dept_id FROM departments WHERE lower(dept_name) = 'technology')),
	('Philin Kotler', (SELECT dept_id FROM departments WHERE lower(dept_name) = 'marketing')),
	('Elon Musk', (SELECT dept_id FROM departments WHERE lower(dept_name) = 'innovation')),
	('Artyom Pavlovets', (SELECT dept_id FROM departments WHERE lower(dept_name) = 'sales'));

INSERT INTO projects(dept_id, project_name)
VALUES 
	((SELECT dept_id FROM departments WHERE lower(dept_name) = 'finance'), 'business logic'),
	((SELECT dept_id FROM departments WHERE lower(dept_name) = 'technology'), 'modernization project'),
	((SELECT dept_id FROM departments WHERE lower(dept_name) = 'marketing'), 'advertising'),
	((SELECT dept_id FROM departments WHERE lower(dept_name) = 'innovation'), 'create new features'),
	((SELECT dept_id FROM departments WHERE lower(dept_name) = 'sales'), 'statistical metods');

INSERT INTO employee_projects (emp_id, project_id)
VALUES
	((SELECT emp_id FROM employees WHERE full_name = 'Larry Fink'), (SELECT project_id FROM projects WHERE project_name = 'business logic')),
	((SELECT emp_id FROM employees WHERE full_name = 'William Gates'), (SELECT project_id FROM projects WHERE project_name = 'modernization project')),
	((SELECT emp_id FROM employees WHERE full_name = 'Philin Kotler'), (SELECT project_id FROM projects WHERE project_name = 'advertising')),
	((SELECT emp_id FROM employees WHERE full_name = 'Elon Musk'), (SELECT project_id FROM projects WHERE project_name = 'create new features')),
	((SELECT emp_id FROM employees WHERE full_name = 'Artyom Pavlovets'), (SELECT project_id FROM projects WHERE project_name = 'statistical metods'));
	
INSERT INTO employee_projects (emp_id, project_id)
VALUES
	((SELECT emp_id FROM employees WHERE full_name = 'Larry Fink'), (SELECT project_id FROM projects WHERE project_name = 'money maker'))
	

INSERT INTO employee_projects (emp_id, project_id)
VALUES
	((SELECT emp_id FROM employees WHERE full_name = 'Cristiano Ronaldo'), (SELECT project_id FROM projects WHERE project_name = 'modernization project'))

	
/* Каскадное удаление и ограничение ссылочной целостности
В таблицах из задачи 1 добавьте правило: при удалении отдела (departments) должны автоматически удаляться все его сотрудники и проекты, 
но записи в employee_projects при этом не должны удаляться автоматически — база должна выдавать ошибку при попытке удаления.
Проверьте поведение каскадов (ON DELETE CASCADE, ON DELETE RESTRICT). */
	
ALTER TABLE employees DROP CONSTRAINT fk_dep_emp;

ALTER TABLE employees
ADD CONSTRAINT fk_dep_emp
FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
ON DELETE CASCADE;

ALTER TABLE projects DROP CONSTRAINT fk_dep_proj;

ALTER TABLE projects
ADD CONSTRAINT fk_dep_proj
FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
ON DELETE CASCADE;

ALTER TABLE employee_projects DROP CONSTRAINT fk_emp;

ALTER TABLE employee_projects
ADD CONSTRAINT fk_emp
FOREIGN KEY (emp_id) REFERENCES employees (emp_id)
ON DELETE RESTRICT;

ALTER TABLE employee_projects DROP CONSTRAINT fk_proj;

ALTER TABLE employee_projects
ADD CONSTRAINT fk_proj
FOREIGN KEY (project_id) REFERENCES projects (project_id)
ON DELETE RESTRICT;

DELETE FROM departments
WHERE dept_name = 'sales'

/* 3.Оптимизация поиска с индексами
Для таблицы employees создайте три индекса:
• по dept_id;
• по full_name;
• составной по (dept_id, full_name).
С помощью EXPLAIN ANALYZE сравните выполнение запросов:
SELECT * FROM employees WHERE dept_id = 10;
SELECT * FROM employees WHERE full_name = 'Ivan Ivanov';
SELECT * FROM employees WHERE dept_id = 10 AND full_name = 'Ivan Ivanov';
Объясните, в каких случаях используется один индекс, составной индекс или оба сразу. */

CREATE TABLE IF NOT EXISTS public.employees1 (
	emp_id serial PRIMARY KEY,
	full_name varchar(50) NOT NULL,
	dept_id int
);

INSERT INTO employees1 (full_name, dept_id)
SELECT
	CASE WHEN i % 5 = 0 THEN 'Ivan Ivanov' ELSE 'Other Other' || i END, i
	FROM generate_series(1, 100000) AS s(i);


CREATE INDEX ix_dept_id ON employees1(dept_id)
CREATE INDEX ix_full_name ON employees1(full_name)
CREATE INDEX ix_dept_id_full_name ON employees1(dept_id, full_name)

EXPLAIN ANALYZE
SELECT * 
FROM employees1 
WHERE dept_id = 10;

EXPLAIN ANALYZE
SELECT * 
FROM employees1 
WHERE full_name = 'Ivan Ivanov';

EXPLAIN ANALYZE
SELECT * 
FROM employees1 
WHERE dept_id = 10 AND full_name = 'Ivan Ivanov';

/* 4. Избыточное индексирование и производительность
Добавьте в таблицу employees ещё один индекс по full_name и сравните результаты вставки 100 000 строк с и без него.
Используйте EXPLAIN ANALYZE INSERT INTO ... SELECT ... для оценки.
Объясните, почему большое количество индексов замедляет операции вставки и обновления, и в каких случаях это оправдано. */

EXPLAIN ANALYZE --375.884
INSERT INTO employees1 (full_name, dept_id)
SELECT
    CASE WHEN i % 5 = 0 THEN 'Ivan Ivanov' ELSE 'Other Other' || i END, i
FROM generate_series(100001, 200000) AS s(i);

CREATE INDEX ix_full_name2 ON employees1(full_name)

EXPLAIN ANALYZE --488.375
INSERT INTO employees1 (full_name, dept_id)
SELECT
    CASE WHEN i % 5 = 0 THEN 'Ivan Ivanov' ELSE 'Other Other' || i END, i
FROM generate_series(200001, 300000) AS s(i);

/* 5. Реальный сценарий выбора оптимального индекса
В таблице projects добавьте поля start_date и budget.
Проанализируйте три типа запросов:
1. фильтр по start_date (диапазон за год),
2. фильтр по budget > 1000000,
3. фильтр одновременно по дате и бюджету.
Создайте подходящие индексы (B-tree или составной) и объясните, какой из них эффективнее для каждого случая и почему. */

CREATE TABLE IF NOT EXISTS public.projects1 (
	project_id serial PRIMARY KEY,
	project_name varchar(50) NOT NULL,
	start_date date NOT NULL,
	budget int NOT NULL 
	);

INSERT INTO projects1 (project_name, start_date, budget)
SELECT
	'Default':: text AS project_name,
	date '2024-01-01' + (random() * 364)::int AS start_date,
	(random() * (1500000 - 500000) + 500000)::int AS budget
	FROM generate_series(1, 100000);

EXPLAIN ANALYZE --22.890 ms
SELECT *
FROM projects1
WHERE start_date BETWEEN '2024-01-01' AND '2024-12-31';

EXPLAIN ANALYZE --15.209 ms
SELECT *
FROM projects1
WHERE budget > 1000000;

EXPLAIN ANALYZE -- 19.591
SELECT *
FROM projects1
WHERE start_date BETWEEN '2024-01-01' AND '2024-12-31' AND budget > 1000000;

CREATE INDEX ix_start_date ON projects1(start_date)
CREATE INDEX ix_budget ON projects1(budget)
CREATE INDEX ix_startdate_budget ON projects1(start_date, budget)

EXPLAIN ANALYZE --8.172
SELECT *
FROM projects1
WHERE start_date BETWEEN '2024-01-01' AND '2024-05-31';

EXPLAIN ANALYZE --15.774
SELECT *
FROM projects1
WHERE start_date BETWEEN '2024-01-01' AND '2024-12-31';


EXPLAIN ANALYZE --13.321
SELECT *
FROM projects1
WHERE budget > 1000000;

EXPLAIN ANALYZE --16.215 ms
SELECT *
FROM projects1
WHERE start_date BETWEEN '2024-01-01' AND '2024-12-31' AND budget > 1000000;

EXPLAIN ANALYZE -- 0.062 ms 
SELECT *
FROM projects1
WHERE start_date = '2024-12-31' AND budget > 1000000;



