import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums_cnt = dict()
nums = []
for _ in range(N):
    num = int(input())
    if num not in nums_cnt:
        nums_cnt[num] = 1
        nums.append(num)
    else:
        nums_cnt[num] += 1

nums.sort()
nums_idx = dict()
nums_idx[nums[0]] = 0
for i in range(1, len(nums)):
    nums_idx[nums[i]] = nums_idx[nums[i-1]] + nums_cnt[nums[i-1]]

for _ in range(M):
    D = int(input())
    if D not in nums_idx:
        print(-1)
    else:
        print(nums_idx[D])