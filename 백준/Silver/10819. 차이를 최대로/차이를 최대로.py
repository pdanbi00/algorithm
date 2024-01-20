def next_perm(nums):
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = len(nums) - 1
    while nums[i-1] >= nums[j]:
        j -= 1
    nums[i-1], nums[j] = nums[j], nums[i-1]
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] =  nums[j], nums[i]
        i += 1
        j -= 1
    return True

def calc(nums):
    total = 0
    for i in range(N-1):
        total += abs(nums[i] - nums[i+1])
    return total

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0

while True:
    temp = calc(nums)
    ans = max(ans, temp)
    if not next_perm(nums):
        break
print(ans)