n = int(input())
podoju = [0] + list(int(input()) for _ in range(n))
dp = [[0]*3 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + podoju[i]
    dp[i][2] = dp[i-1][1] + podoju[i]
print(max(dp[n]))