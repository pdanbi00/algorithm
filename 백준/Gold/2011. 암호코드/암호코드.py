nums = input()
N = len(nums)
dp = [0] * N

if int(nums[0]) >= 1:
    dp[0] = 1
    dp[0] %= 1000000
if N >= 2:
    if int(nums[1]) >= 1:
        dp[1] += 1
    if int(nums[0:2]) >= 10 and int(nums[0:2]) <= 26:
        dp[1] += 1
    dp[1] %= 1000000
if N >= 2:
    for i in range(2, N):
        if int(nums[i]) >= 1:
            dp[i] += dp[i-1]
        if int(nums[i-1:i+1]) >= 10 and int(nums[i-1:i+1]) <= 26:
            dp[i] += dp[i-2]
        dp[i] %= 1000000
if min(dp) == 0:
    print(0)
else:
    print(dp[N-1])

