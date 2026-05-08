--M27-L6

/*
Задание 6.1
Сколько вакансий имеет отношение к данным
*/

--SELECT DISTINCT COUNT(*) AS data_vacancies_count
--FROM public.vacancies
--WHERE LOWER(vacancies.name) LIKE LOWER('%data%') OR LOWER(vacancies.name) LIKE LOWER('%данн%')

/*
Задание 6.2
Сколько есть подходящих вакансий для начинающего дата-сайентиста?

Будем считать вакансиями для дата-сайентистов такие, в названии которых есть хотя бы одно из следующих сочетаний:

‘data scientist’;
‘data science’;
‘исследователь данных’;
‘ML’ (здесь не нужно брать вакансии по HTML);
‘machine learning’;
‘машинн%обучен%’.
В следующих заданиях мы продолжим работать с вакансиями по указанному выше условию (уже не учитывая вакансии уровня Junior).

Считаем вакансиями для специалистов уровня Junior следующие:

в названии есть слово “junior” или
требуемый опыт — «Нет опыта» или
тип трудоустройства — «Стажировка».
В качестве ответа запишите количество вакансий, которое вернул запрос.
*/
--WITH ds_vacancies AS (
--	SELECT * --vacancies.name --  COUNT(*) AS data_vacancies_count
--	FROM public.vacancies
--	WHERE LOWER(vacancies.name) LIKE LOWER('%data scientist%') OR
--		LOWER(vacancies.name) LIKE LOWER('%data science%') OR
--		LOWER(vacancies.name) LIKE LOWER('%исследователь данных%') OR
--		(LOWER(vacancies.name) LIKE LOWER('%ML%') AND LOWER(vacancies.name) NOT LIKE LOWER('%HTML%')) OR
--		LOWER(vacancies.name) LIKE LOWER('%machine learning%') OR
--		LOWER(vacancies.name) LIKE LOWER('%машинн%обучен%')
--	ORDER BY vacancies.name
--)
--SELECT COUNT(*) AS vacancies_count
--FROM ds_vacancies
--WHERE LOWER(ds_vacancies.name) LIKE LOWER('%Junior%') OR 
--(ds_vacancies.experience = 'Нет опыта' OR ds_vacancies.employment = 'Стажировка' )


/*
Задание 6.3
Сколько есть вакансий для DS, в которых в качестве ключевого навыка указан SQL или postgres?
В качестве ответа запишите количество, которое вернул запрос.
*/

--WITH ds_vacancies AS (
--	SELECT * 
--	FROM public.vacancies
--	WHERE LOWER(vacancies.name) LIKE LOWER('%data scientist%') OR
--		LOWER(vacancies.name) LIKE LOWER('%data science%') OR
--		LOWER(vacancies.name) LIKE LOWER('%исследователь данных%') OR
--		(LOWER(vacancies.name) LIKE LOWER('%ML%') AND LOWER(vacancies.name) NOT LIKE LOWER('%HTML%')) OR
--		LOWER(vacancies.name) LIKE LOWER('%machine learning%') OR
--		LOWER(vacancies.name) LIKE LOWER('%машинн%обучен%')
--	ORDER BY vacancies.name
--)
--SELECT COUNT(*) AS vacancies_count
--FROM ds_vacancies
--WHERE LOWER(ds_vacancies.key_skills) LIKE LOWER('%SQL%') OR LOWER(ds_vacancies.key_skills) LIKE LOWER('%postgres%')


/*
Задание 6.4
С помощью запроса, аналогичного предыдущему, проверьте, насколько популярен Python в требованиях работодателей к DS. Вычислите количество вакансий, в которых в качестве ключевого навыка указан Python.
В качестве ответа запишите количество, которое вернул запрос.
*/

--WITH ds_vacancies AS (
--	SELECT * 
--	FROM public.vacancies
--	WHERE LOWER(vacancies.name) LIKE LOWER('%data scientist%') OR
--		LOWER(vacancies.name) LIKE LOWER('%data science%') OR
--		LOWER(vacancies.name) LIKE LOWER('%исследователь данных%') OR
--		(LOWER(vacancies.name) LIKE LOWER('%ML%') AND LOWER(vacancies.name) NOT LIKE LOWER('%HTML%')) OR
--		LOWER(vacancies.name) LIKE LOWER('%machine learning%') OR
--		LOWER(vacancies.name) LIKE LOWER('%машинн%обучен%')
--	ORDER BY vacancies.name
--)
--SELECT COUNT(*) AS vacancies_count
--FROM ds_vacancies
--WHERE LOWER(ds_vacancies.key_skills) LIKE LOWER('%Python%')

/*
Задание 6.5
Сколько ключевых навыков в среднем указывают в вакансиях для DS?
Ответ округлите до двух знаков после точки-разделителя.
*/

/*
WITH ds_vacancies AS (
	SELECT * 
	FROM public.vacancies
	WHERE LOWER(vacancies.name) LIKE LOWER('%data scientist%') OR
		LOWER(vacancies.name) LIKE LOWER('%data science%') OR
		LOWER(vacancies.name) LIKE LOWER('%исследователь данных%') OR
		--чтобы ответ сходился
		((vacancies.name) LIKE ('%ML%') AND LOWER(vacancies.name) NOT LIKE LOWER('%HTML%')) OR
		LOWER(vacancies.name) LIKE LOWER('%machine learning%') OR
		LOWER(vacancies.name) LIKE LOWER('%машинн%обучен%')
	ORDER BY vacancies.name
)
/*
-- вся таблица  key_skills со счетчиком skills_count
SELECT  ds_vacancies.key_skills,
	--решение только для PostgreSQL
    ARRAY_LENGTH(STRING_TO_ARRAY(ds_vacancies.key_skills, CHR(9)),1) AS skills_count
FROM ds_vacancies
ORDER BY skills_count DESC
*/
-- Считаем среднее
-- Решение только для PostgreSQL
-- Разделитель '/t' или CHR(9). Делим сроку по табу, считаем длинну массиса, округляем.
SELECT ROUND(AVG(ARRAY_LENGTH(STRING_TO_ARRAY(ds_vacancies.key_skills, CHR(9)),1)),2) AS avg_skills_count
FROM ds_vacancies
*/

/*
Задание 6.6
Напишите запрос, позволяющий вычислить, какую зарплату для DS в среднем указывают для каждого типа требуемого опыта
(уникальное значение из поля experience).
При решении задачи примите во внимание следующее:

1 Рассматриваем только вакансии, у которых заполнено хотя бы одно из двух полей с зарплатой.
2 Если заполнены оба поля с зарплатой, считаем зарплату по каждой вакансии как сумму двух полей, делённую на 2. Если заполнено только одно из полей, его и считаем зарплатой по вакансии.
3 Если в расчётах участвует null, в результате он тоже даст null (посмотрите, что возвращает запрос select 1 + null).
4 Чтобы избежать этой ситуации, мы воспользуемся функцией coalesce, которая заменит null на значение, которое мы передадим. Например, посмотрите, что возвращает запрос select 1 + coalesce(null, 0).
*/

WITH ds_vacancies AS (
	SELECT * 
	FROM public.vacancies
	WHERE LOWER(vacancies.name) LIKE LOWER('%data scientist%') OR
		LOWER(vacancies.name) LIKE LOWER('%data science%') OR
		LOWER(vacancies.name) LIKE LOWER('%исследователь данных%') OR
		--чтобы ответ сходился
		((vacancies.name) LIKE ('%ML%') AND LOWER(vacancies.name) NOT LIKE LOWER('%HTML%')) OR
		LOWER(vacancies.name) LIKE LOWER('%machine learning%') OR
		LOWER(vacancies.name) LIKE LOWER('%машинн%обучен%')
	ORDER BY vacancies.name
)

/*
вычисляем среднюю зарплату как среднее между salary_from и salary_to
COALESCE обрабатывает случаи, когда одно из полей равно NULL
- если средняя зарплата посчиталась (оба поля заполнены) — берётся она;
- если salary_to равно NULL — берётся salary_from
- если salary_from равно NULL — берётся salary_to
*/
SELECT ds_vacancies.experience, ROUND(AVG(COALESCE((ds_vacancies.salary_from + ds_vacancies.salary_to)/2, ds_vacancies.salary_from, ds_vacancies.salary_to)),0) AS salary_avg
FROM ds_vacancies
GROUP BY ds_vacancies.experience
ORDER BY salary_avg DESC


