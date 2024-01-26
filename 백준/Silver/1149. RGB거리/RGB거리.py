# 0 : 빨강    1 : 초록     2: 파랑
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N+1)]
dp[1][0] = colors[0][0]
dp[1][1] = colors[0][1]
dp[1][2] = colors[0][2]
for i in range(2, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + colors[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + colors[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + colors[i-1][2]
print(min(dp[N]))