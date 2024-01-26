MAX = 1000000
dp = [0] * (MAX+1)
dp[0] = 1
for i in range(1, MAX+1):
    if i - 1 >= 0:
        dp[i] += dp[i-1]
    if i - 2 >= 0:
        dp[i] += dp[i-2]
    if i - 3 >= 0:
        dp[i] += dp[i-3]
    dp[i] %= 1000000009

T = int(input())
for tc in range(T):
    n = int(input())
    print(dp[n])