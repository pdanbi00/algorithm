SELECT WRITER_ID, NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS A
INNER JOIN USED_GOODS_USER AS B
ON A.WRITER_ID = B.USER_ID
WHERE STATUS = 'DONE'
GROUP BY WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES
