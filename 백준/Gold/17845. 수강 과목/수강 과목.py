import sys
input = sys.stdin.readline

N, K = map(int, input().split())
study = [list(map(int, input().split())) for _ in range(K)]

dp = [[0] * (N+1) for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(1, N+1):
        if j - study[i-1][1] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-study[i-1][1]] + study[i-1][0])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[K][N])