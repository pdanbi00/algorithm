N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
ans = 0
for i in range(N):
    if K // coins[i] >= 1:
        ans += K // coins[i]
        K = K % coins[i]
print(ans)
