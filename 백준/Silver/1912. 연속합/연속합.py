n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = nums[i]
    if dp[i-1] + nums[i] > dp[i]:
        dp[i] = dp[i-1] + nums[i]

print(max(dp))