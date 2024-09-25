N = int(input())

dp = [0] * 1000001
dp[0] = 1
dp[1] = 2
dp[2] = 7
dp_sum = sum(dp[:3])
# N이 3일때를 잘 생각 해봐야 됨.

# 3부터 위아래로 세로줄이 안 겹치는 타일이 2개씩 등장함
# dp[i] = (2 * dp[i-1] + 3 * dp[i-2] + 2 * dp[i-3] + ... + 2 * dp[1]) % 1000000007
# -> dp[i] = 2 * sum(dp[i-1]) + dp[i-2]
for i in range(3, N+1):
    dp[i] = 2 * dp_sum + dp[i-2]
    dp[i] %= 1000000007
    dp_sum += dp[i]
print(dp[N])