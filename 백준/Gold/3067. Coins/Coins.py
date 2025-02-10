T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N+1):
        dp[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j]
            if j - coins[i-1] >= 0:
                dp[i][j] += dp[i][j-coins[i-1]]

    print(dp[N][M])