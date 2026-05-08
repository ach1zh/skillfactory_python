CREATE TABLE testTable(
	id SERIAL PRIMARY KEY, -- первичный ключ
	name TEXT NOT NULL, -- название товара
	user_id BIGINT UNIQUE,
	text VARCHAR(1000) 
);

CREATE TABLE posts(
	id SERIAL PRIMARY KEY, -- первичный ключ
	author TEXT UNIQUE NOT NULL,
	content TEXT NOT NULL
);