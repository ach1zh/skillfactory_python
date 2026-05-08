-- просмотр всех таблиц в схеме public
SELECT * FROM pg_catalog.pg_tables WHERE schemaname = 'public';


--Переименование столбца
--
-- переименование таблицы posts в posts1
--ALTER TABLE posts RENAME TO posts1;
-- проверка
--SELECT * FROM pg_catalog.pg_tables WHERE schemaname = 'public';
--
-- переименование таблицы posts1 в posts
--ALTER TABLE posts1 RENAME TO posts;
-- проверка
--SELECT * FROM pg_catalog.pg_tables WHERE schemaname = 'public';


--Добавление столбца
-- добавление столбца "дата публикации", хранящим время в формате Unix Time
ALTER TABLE posts ADD COLUMN IF NOT EXISTS publication_date BIGINT NOT NULL;
-- просмотр столбцов таблицы - проверка
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_name = 'posts';

--Добавление ограничения
-- добавление ограничения уникальности для столбца с датой публикации
ALTER TABLE posts ADD CONSTRAINT pub_date_unique UNIQUE(publication_date);