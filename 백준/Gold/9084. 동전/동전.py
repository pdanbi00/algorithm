T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1 # 0원을 만드는 경우의 수는 1개
    for coin in coins:
        for money in range(1, M+1):
            if money >= coin:
                dp[money] += dp[money-coin]
    print(dp[M])
