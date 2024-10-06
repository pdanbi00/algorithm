N, D = map(int, input().split())
dp = [i for i in range(D+1)]
shortcuts = []
for _ in range(N):
    start, end, distance = map(int, input().split())
    if end - start > distance:
        shortcuts.append((start, end, distance))
shortcuts.sort()

for start, end, distance in shortcuts:
    for i in range(1, D+1):
        if end == i:
            dp[i] = min(dp[i], dp[start] + distance)
        else:
            dp[i] = min(dp[i], dp[i-1] + 1)
print(dp[D])