N, K = map(int, input().split())
dp = [[0] * (N+1) for _ in range(K+1)]
dp[0][0] = 1
for i in range(1, K+1):
    for j in range(N+1):
        for l in range(j+1):
            if i == 1:
                dp[i][j] = 1
            else:
                dp[i][j] += dp[i-1][j-l]
                dp[i][j] %= 1000000000
print(dp[K][N] % 1000000000)