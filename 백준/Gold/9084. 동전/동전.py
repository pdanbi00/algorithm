T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    money = int(input())

    # dp[i] : i원을 만들 수 있는 가지수

    dp = [0] * (money+1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, money+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[money])