N = int(input())
dp = [[0] * 10 for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= 10007
print(sum(dp[N]) % 10007)