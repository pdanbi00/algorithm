N = int(input())
nums = list(map(int, input().split()))
dp = [0] * N
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if nums[i] < nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))