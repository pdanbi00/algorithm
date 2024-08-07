-- 코드를 입력하세요
# 0시부터 23시까지 생성
SET @HOUR = -1;
SELECT (@HOUR := @HOUR + 1) AS HOUR, 
    (SELECT COUNT(HOUR(DATETIME))
     FROM ANIMAL_OUTS
     WHERE HOUR(DATETIME) = @HOUR) AS COUNT
    FROM ANIMAL_OUTS
WHERE @HOUR < 23;

# SELECT HOUR(DATETIME) AS HOUR, 0COUNT(ANIMAL_ID) AS COUNT
# FROM ANIMAL_OUTS
# GROUP BY HOUR(DATETIME)
# ORDER BY HOUR(DATETIME)

# SELECT A.ANIMAL_ID, A.DATETIME, 0 AS NEW_MONTH
# FROM ANIMAL_OUTS A