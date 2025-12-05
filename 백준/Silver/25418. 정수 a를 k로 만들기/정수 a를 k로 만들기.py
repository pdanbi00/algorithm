A, K = map(int, input().split())

dp = [1e9] * (K+1)
dp[A] = 0

for i in range(A, K+1):
    new_num = i * 2
    if new_num <= K:
        dp[new_num] = min(dp[new_num], dp[i] + 1)

    new_num = i + 1
    if new_num <= K:
        dp[new_num] = min(dp[new_num], dp[i] + 1)

print(dp[K])