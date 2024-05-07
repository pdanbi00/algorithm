nums = [i for i in range(1, 21)]

for j in range(10):
    start, end = map(int, input().split())
    reverse_arr = nums[start-1:end]
    reverse_arr.reverse()
    nums = nums[:start-1] + reverse_arr + nums[end:]
print(*nums)