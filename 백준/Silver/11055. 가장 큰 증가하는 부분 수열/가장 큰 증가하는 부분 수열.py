# dp[i]는 nums의 i번째로 끝나는 증가하는 부분 수열 중의 합 중 가장 큰 값
N = int(input())
nums = list(map(int, input().split()))
dp = [0] * (N)
for i in range(N):
    dp[i] = nums[i]
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
            dp[i] = dp[j] + nums[i]
# 무조건 제일 마지막꺼가 가장 큰게 아님
# 증가하는 부분수열이기 때문에 중간에 끝난게 합이 더 클 수 있어서 max로 값 찾아줘야 됨.
print(max(dp))