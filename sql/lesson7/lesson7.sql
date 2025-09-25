/* Создать базу данных library, внутри неё таблицу books с полями: book_id (целое число, первичный ключ, автоинкремент), 
 title (строка до 200 символов, не пустая), author (строка до 100 символов), published_year (целое число, год издания). 
 После этого добавить в таблицу три книги. */


CREATE DATABASE some_library;

CREATE TABLE IF NOT EXISTS books (
	book_id SERIAL PRIMARY KEY,
	title varchar(200) NOT NULL,
	author varchar(100),
	published_year int
	);

INSERT INTO books (title, author, published_year)
VALUES ('Harry Potter and the prisioner of azkhaban', 'J.K. Rowling', 1999),
	   ('For whom the bell tolls ', 'Ernest Homingway', 1940),
	   ('The man who laughs', 'Victor Hugo', 1869);

/* В таблице books нужно изменить структуру: добавить новый столбец genre типа VARCHAR(50), переименовать столбец title в book_title, 
а затем удалить столбец published_year. */

ALTER TABLE books 
	ADD COLUMN genre varchar(50);

ALTER TABLE books
	RENAME COLUMN title
	TO book_title;

ALTER TABLE books
	DROP COLUMN published_year;


/* В таблице books удалить все записи, где автор равен 'Unknown'. 
 Создать таблицу archived_books с теми же полями, что и у books, перенести в неё все книги автора 'J.K. Rowling', 
 после чего полностью удалить таблицу archived_books. */

DELETE 
FROM books
WHERE author = 'Unknown';
	
CREATE TABLE archived_books AS
SELECT * 
FROM books
WHERE author = 'J.K. Rowling';

DROP TABLE IF EXISTS archived_books;


