CREATE TABLE IF NOT EXISTS movies (
	movie_id serial PRIMARY KEY,
	title text NOT NULL,
	genre text NOT NULL,
	release_year int,
	duration int
);

CREATE TABLE IF NOT EXISTS tickets (
	ticket_id serial PRIMARY KEY,
	movie_id int,
	customer_name text NOT NULL,
	seat_number int NOT NULL,
	price int NOT NULL,
	FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);

INSERT INTO movies (title, genre, release_year, duration)
VALUES 
	('Джентльмены', 'Приключения', 2018, 141),
	('Прометей', 'Фантастика', 2017, 122),
	('Пираты Карибского моря', 'Приключения', 2013, 180),
	('Пчеловод', 'Боевик', 2024, 113),
	('Голый пистолет', 'Комедия', 2025, 99);

INSERT INTO tickets (movie_id, customer_name, seat_number, price)
VALUES 
	(1, 'Иванов Петр', 4, 13),
	(2, 'Багров Даниил', 11, 15),
	(3, 'Кириленко Степан', 33, 22),
	(1, 'Антонова Антонина', 25, 16),
	(5, 'Артемов Артем', 44, 30);

SELECT title
FROM movies m
WHERE m.genre = 'Приключения';

SELECT *
FROM movies m
WHERE m.release_year > 2020;

SELECT *
FROM tickets t
WHERE t.price > 15;

SELECT *
FROM movies m
WHERE m.title LIKE '%Пираты%';
