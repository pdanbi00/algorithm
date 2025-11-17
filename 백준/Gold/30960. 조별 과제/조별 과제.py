N = int(input())
nums = list(map(int, input().split()))
nums.sort()

total = nums[2] - nums[0]
for i in range(4, N, 2):
    total += nums[i] - nums[i-1]

ans = total

for i in range(2, N-1, 2):
    total -= nums[i] - nums[i-2]
    total -= nums[i+2] - nums[i+1]
    total += nums[i-1] - nums[i-2]
    total += nums[i+2] - nums[i]

    ans = min(ans, total)
print(ans)