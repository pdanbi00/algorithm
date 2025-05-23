SELECT C.CATEGORY, SUM(C.SALES) AS TOTAL_SALES
FROM (
    SELECT A.BOOK_ID, B.CATEGORY, A.SALES_DATE, A.SALES
    FROM BOOK_SALES AS A
    LEFT JOIN BOOK AS B
    ON A.BOOK_ID = B.BOOK_ID
    WHERE YEAR(A.SALES_DATE) = 2022 AND MONTH(A.SALES_DATE) = 1
) AS C
GROUP BY C.CATEGORY
ORDER BY C.CATEGORY
