# 방법 2 : 부분합
N, M = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(1, N):
    nums[i] += nums[i-1]
nums = [0] + nums
cnt = 0
for i in range(N+1):
    for j in range(i, N+1):
        if nums[j] - nums[i] == M:
            cnt += 1
print(cnt)