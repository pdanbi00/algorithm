import sys
input = sys.stdin.readline
while True:
    n, money = map(float, input().rstrip().rsplit())
    n = int(n)
    if n == 0 and money == 0.00:
        break
    money = int(money * 100)
    candies = []
    for _ in range(n):
        c, p = map(float, input().rstrip().rsplit())
        candies.append((int(c), int(p * 100 + 0.5))) # 0.5를 더해주는 이유는 부동소수점 오류 방지

    dp = [0] * (money+1)
    # dp[i] : 돈이 i일때 사탕 중 가장 높은 칼로리
    for i in range(1, money+1):
        for j in range(n):
            candy_cal = candies[j][0]
            candy_price = candies[j][1]

            if i < candy_price:
                continue
            dp[i] = max(dp[i], dp[i-candy_price] + candy_cal)
    print(dp[money])