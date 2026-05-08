--Удаление БД:
DROP database db_name;

--Удаление таблицы:
DROP TABLE IF EXISTS some_table;

--Удаление столбца:
-- удаление столбца с датой публикации из таблицы
ALTER TABLE posts DROP COLUMN publication_date;