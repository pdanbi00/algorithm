T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(nums[2])