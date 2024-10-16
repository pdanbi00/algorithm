SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT A.USER_ID) AS USERS
FROM ONLINE_SALE AS A
INNER JOIN USER_INFO AS B
ON A.USER_ID = B.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER
ORDER BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER;