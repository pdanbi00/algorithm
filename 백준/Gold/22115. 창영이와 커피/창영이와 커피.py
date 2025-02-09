N, K = map(int, input().split())
coffee = list(map(int, input().split()))

dp = [[1e9] * (K+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = 0

for i in range(1, N+1):
    for j in range(1, K+1):
        if j - coffee[i-1] >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-coffee[i-1]] + 1)
        else:
            dp[i][j] = dp[i-1][j]
if dp[N][K] == 1e9:
    print(-1)
else:
    print(dp[N][K])
