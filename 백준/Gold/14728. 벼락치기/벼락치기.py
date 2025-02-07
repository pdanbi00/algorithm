N, T = map(int, input().split())
study = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (T+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, T+1):
        if j - study[i-1][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-study[i-1][0]] + study[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][T])