n = int(input())
dp = [0] * 100001

dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, n+1):
    if i - 2 >= 0 and dp[i-2] > 0:
        dp[i] = dp[i-2] + 1

    if i - 5 >= 0 and dp[i-5] > 0:
        dp[i] = min(dp[i], dp[i-5] + 1)

if dp[n] == 0:
    print(-1)
else:
    print(dp[n])