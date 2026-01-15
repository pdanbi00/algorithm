N, K = map(int, input().split())

dp = [1] * (N+1)

for i in range(1, N+1):
    dp[i] = dp[i-1] * K
    if i >= 5:
        dp[i] -= dp[i-5] * 2 # 패턴 길이가 5니깐 두 종류 해서
    # ABCBC, ABABC인데 ABABCBC로 겹칠 수 있음
    if i >= 7:
        dp[i] += dp[i-7]
    dp[i] %= 1000000009
print(dp[N])