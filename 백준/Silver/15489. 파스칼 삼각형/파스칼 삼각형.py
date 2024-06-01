dp = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    dp[i][0] = 1
    dp[i][i-1] = 1
# print(dp)
for i in range(2, 31):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
R, C, W = map(int, input().split())
ans = 0
cnt = 0
for i in range(W):
    for j in range(i+1):
        ans += dp[R+i][C-1+j]
print(ans)
# print(ans, cnt)
