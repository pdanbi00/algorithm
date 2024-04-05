n, k = map(int, input().split())
dp = [0] * (k+1)

coin = []
for i in range(n):
    num = int(input())
    if num <= k:
        coin.append(num)
coin.sort()
dp[0] = 1 # 동전이 3이라면 dp[0]은 dp[3-3]이라고 생각.
for c in coin:
    for j in range(c, k+1):
        dp[j] += dp[j-c]
print(dp[k])
