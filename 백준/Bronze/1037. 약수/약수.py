N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(max(nums) * min(nums))