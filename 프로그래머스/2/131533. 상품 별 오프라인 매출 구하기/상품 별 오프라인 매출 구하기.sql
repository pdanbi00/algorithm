-- 코드를 입력하세요
SELECT B.PRODUCT_CODE, SUM(B.PRICE * A.SALES_AMOUNT) AS SALES
FROM OFFLINE_SALE AS A
INNER JOIN PRODUCT AS B
ON A.PRODUCT_ID = B.PRODUCT_ID
GROUP BY B.PRODUCT_CODE
ORDER BY SALES DESC, B.PRODUCT_CODE;