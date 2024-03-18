n, k = map(int, input().split())
coin = set()
for i in range(n):
    cost = int(input())
    coin.add(cost)
dp = [100001] * 10001
for c in coin:
    if c <= 10000:
        dp[c] = 1
for i in range(1, k+1):
    for c in coin:
        if i-c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)
if dp[k] != 100001:
    print(dp[k])
else:
    print(-1)