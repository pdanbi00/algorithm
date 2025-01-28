N = int(input())
nums = list(map(int, input().split()))

answer = 0
target = nums[-1]

dp = [[0] * 21 for _ in range(N)]
dp[0][nums[0]] = 1

for i in range(1, len(nums)-1):
    for j in range(21):
        if dp[i-1][j] > 0:
            tmp1 = j + nums[i]
            tmp2 = j - nums[i]
            if 0 <= tmp1 <= 20:
                dp[i][tmp1] += dp[i-1][j]
            if 0 <= tmp2 <= 20:
                dp[i][tmp2] += dp[i-1][j]
# print(dp)
print(dp[N-2][target])