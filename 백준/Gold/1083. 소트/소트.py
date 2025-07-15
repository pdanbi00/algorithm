N = int(input())
nums = list(map(int, input().split()))
S = int(input())
for i in range(N):
    if not S:
        break
    max_val = max(nums[i:i+S+1])
    max_idx = nums.index(max_val)
    while max_idx > i and S:
        nums[max_idx], nums[max_idx-1] = nums[max_idx-1], nums[max_idx]
        max_idx -= 1
        S -= 1
print(*nums)