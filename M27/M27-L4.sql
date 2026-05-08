--M27-L4

/*
Задание 4.1
1. Напишите запрос, который позволит узнать, сколько (cnt) вакансий в каждом регионе (area).
Отсортируйте по количеству вакансий в порядке убывания.
*/

--SELECT areas.name AS area_name, COUNT(vacancies.id) AS vacancies_count 
--FROM  public.vacancies
--LEFT JOIN public.areas ON vacancies.area_id = areas.id
--GROUP BY areas.id
--ORDER BY vacancies_count DESC;

/*
Задание 4.2
Посмотрим на зарплаты. У какого количества вакансий заполнено хотя бы одно из двух полей с зарплатой?
*/

----SELECT vacancies.id, vacancies.salary_from, vacancies.salary_to
--SELECT COUNT(*) AS vacancies_with_salary
--FROM public.vacancies
--WHERE vacancies.salary_from IS NOT NULL OR vacancies.salary_to IS NOT NULL;

/*
Задание 4.3
Найдите средние значения для нижней и верхней границы зарплатной вилки. Округлите значения до целого числа.
*/

--SELECT round(avg(vacancies.salary_from)) AS salary_from, round(avg(vacancies.salary_to)) AS salary_to
--FROM public.vacancies

/*
Задание 4.4
Напишите запрос, который выведет количество вакансий для каждого сочетания типа рабочего графика (schedule)
и типа трудоустройства (employment), используемого в вакансиях. Какая пара находится на втором месте по популярности?
*/

--SELECT vacancies.schedule, vacancies.employment, COUNT(*) AS vacancies_count
--FROM public.vacancies
--GROUP BY vacancies.schedule, vacancies.employment
--ORDER BY vacancies_count DESC
--LIMIT 10;


/*
Задание 4.5
Напишите запрос, выводящий значения поля Требуемый опыт работы (experience) в порядке возрастания
количества вакансий, в которых указан данный вариант опыта.
*/

SELECT vacancies.experience , COUNT(*) AS vacancies_count
FROM public.vacancies
GROUP BY vacancies.experience
ORDER BY vacancies_count;
