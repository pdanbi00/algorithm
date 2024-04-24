n = int(input())

dp = [0] * 1000001
dp[1] = 1

if n < 0:
    for i in range(2, abs(n)+1):
        dp[i] = dp[i-2] - dp[i-1]
        if dp[i] < 0:
            dp[i] = abs(dp[i]) % 1000000000
            dp[i] *= -1
        else:
            dp[i] = dp[i] % 1000000000
elif n > 0:
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000000

if n >= 0:
    if dp[n] > 0:
        print(1)
    else:
        print(0)
    print(dp[n])
else:
    if dp[abs(n)] > 0:
        print(1)
    elif dp[abs(n)] == 0:
        print(0)
    else:
        print(-1)
    print(abs(dp[abs(n)]))