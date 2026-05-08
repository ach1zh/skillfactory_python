

	/*
    SELECT employers.name , count(employers_industries.industry_id) AS industry_id_count
    FROM public.employers_industries
    LEFT JOIN public.employers ON employers.id = employers_industries.employer_id
    GROUP BY employers.name
    HAVING count(employers_industries.industry_id) = 4
    ORDER BY employers.name;
	*/

	
--SELECT ROUND(AVG(industry_id_count), 2) AS avg_industry_per_employer
--FROM (
--    SELECT employers.name, COUNT(employers_industries.industry_id) AS industry_id_count
--    FROM public.employers_industries
--    LEFT JOIN public.employers ON employers.id = employers_industries.employer_id
--    GROUP BY employers.name
--) AS employer_industry_counts;


SELECT industry_id_count AS number_of_industries,
	COUNT(*) AS number_of_employers,
    ROUND(AVG(industry_id_count), 2) AS average_per_group
FROM (
    SELECT employers.name, COUNT(employers_industries.industry_id) AS industry_id_count
    FROM public.employers_industries
    LEFT JOIN public.employers ON employers.id = employers_industries.employer_id
    GROUP BY employers.name
) AS employer_industry_counts
GROUP BY industry_id_count
ORDER BY number_of_industries;