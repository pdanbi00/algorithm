N, K = map(int, input().split())
nums = [[0] * N for _ in range(N)]
nums[0][0] = 1

for i in range(1, N):
    nums[i][0] = 1
    nums[i][i] = 1
    for j in range(1, i):
        nums[i][j] = nums[i-1][j-1] + nums[i-1][j]
# print(nums)
print(nums[N-1][K-1])