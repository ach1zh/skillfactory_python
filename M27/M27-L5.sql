--M27-L5

/*
Задание 5.1
Напишите запрос, который позволит узнать, какие работодатели находятся на первом и пятом месте по количеству вакансий.
*/

--v1
--SELECT employers.name, COUNT(*) AS vacancies_count
--FROM public.vacancies
--LEFT JOIN public.employers ON employers.id = vacancies.employer_id
--GROUP BY employers.id
--ORDER BY vacancies_count DESC;

--v2
--SELECT employers.name, COUNT(*) AS vacancies_count
--FROM public.employers
--JOIN public.vacancies ON vacancies.employer_id = employers.id
--GROUP BY employers.id
--ORDER BY vacancies_count DESC
--LIMIT 10;

/*
Задание 5.2
Напишите запрос, который для каждого региона выведет количество работодателей и вакансий в нём.
Среди регионов, в которых нет вакансий, найдите тот, в котором наибольшее количество работодателей.
Впишите его название в поле ниже в том виде, который вернул запрос.
*/

--SELECT areas.name AS area_name, COUNT(employers.id) AS employers_count, COUNT(vacancies.id) AS vacancies_count
--FROM public.areas
--LEFT JOIN public.employers ON areas.id = employers.area
--LEFT JOIN public.vacancies ON areas.id = vacancies.area_id
----WHERE vacancies.id is null
--GROUP BY areas.id
--ORDER BY vacancies_count, employers_count DESC

/*
Задание 5.3
Для каждого работодателя посчитайте количество регионов, в которых он публикует свои вакансии.
Выберите максимальное значение из получившегося списка.
*/

--SELECT employers.name AS employers_name, COUNT(DISTINCT vacancies.area_id) AS areas_count
--FROM public.employers
--LEFT JOIN public.vacancies ON vacancies.employer_id = employers.id
--GROUP BY employers.name
--ORDER BY areas_count DESC

/*
Задание 5.4
Напишите запрос для подсчёта количества работодателей, у которых не указана сфера деятельности.
Введите количество, которое вернул запрос, в поле ниже.
*/

-- !!! count(*) считает строки с null, COUNT(column) считает только строки IS NOT NULL
--SELECT count(*) AS employer_id_null_count
--FROM public.employers
--LEFT JOIN public.employers_industries ON employers_industries.employer_id = employers.id
--WHERE employers_industries.employer_id is null

/*
Задание 5.5
Напишите запрос, чтобы узнать название компании, находящейся на третьем месте в алфавитном списке (по названию) компаний,
у которых указано четыре сферы деятельности.
Введите в поле ниже название этой компании так же, как оно указано в результате запроса.
*/

--SELECT employers.name , count(employers_industries.industry_id) AS industry_id_count
--FROM public.employers_industries
--LEFT JOIN public.employers ON employers.id = employers_industries.employer_id
--GROUP BY employers.name
--HAVING count(employers_industries.industry_id) = 4
--ORDER BY employers.name

/*
Задание 5.6
С помощью запроса выясните, у какого количества работодателей в качестве сферы 
деятельности указана «Разработка программного обеспечения».
*/

--v1
--SELECT industries.name, count(*) AS employers_count
--FROM public.employers_industries
--LEFT JOIN public.industries ON industries.id = employers_industries.industry_id
--WHERE industries.name = 'Разработка программного обеспечения'
--GROUP BY industries.name

--v2
--SELECT count(*) AS employers_count
--FROM public.employers_industries
--LEFT JOIN public.industries ON industries.id = employers_industries.industry_id
--WHERE industries.name = 'Разработка программного обеспечения'

/*
Задание 5.7
Для компании «Яндекс» выведите список регионов-миллионников, в которых представлены вакансии компании, 
вместе с количеством вакансий в этих регионах. Также добавьте строку Total с общим количеством вакансий компании, 
собранных в этой таблице. Должна получиться выборка такого вида (приведён пример результата для компании SberTech):
*/

--('Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Красноярск', 'Нижний Новгород', 'Челябинск', 'Уфа', 'Краснодар', 'Самара', 'Ростов-на-Дону', 'Омск', 'Воронеж', 'Пермь', 'Волгоград')


SELECT areas.name, count(*) AS vacancies_count
FROM public.vacancies
JOIN public.employers ON employers.id = vacancies.employer_id
JOIN  public.areas ON areas.id = vacancies.area_id
WHERE employers.name = 'Яндекс' 
	AND areas.name IN ('Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Красноярск', 'Нижний Новгород', 'Челябинск', 'Уфа', 'Краснодар', 'Самара', 'Ростов-на-Дону', 'Омск', 'Воронеж', 'Пермь', 'Волгоград')
GROUP BY areas.name

UNION ALL (
	SELECT 'TOTAL' AS name, COUNT(*) AS vacancies_count
	FROM public.vacancies
	JOIN public.employers ON employers.id = vacancies.employer_id
	JOIN public.areas ON areas.id = vacancies.area_id
	WHERE employers.name = 'Яндекс'
		AND areas.name IN ('Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Красноярск', 'Нижний Новгород', 'Челябинск', 'Уфа', 'Краснодар', 'Самара', 'Ростов-на-Дону', 'Омск', 'Воронеж', 'Пермь', 'Волгоград')
	)
	
ORDER BY vacancies_count