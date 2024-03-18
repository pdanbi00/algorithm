n, k = map(int, input().split())
coin = set()
for i in range(n):
    coin.add(int(input()))
dp = [10001] * (k+1)
for c in coin:
    if c <= k:
        dp[c] = 1
for i in range(k+1):
    for c in coin:
        if i-c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)
if dp[k] != 10001:
    print(dp[k])
else:
    print(-1)