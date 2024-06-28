n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()
ans = 0

start = 0
end = n-1
while start < end:
    if nums[start] + nums[end] == x:
        ans += 1
        start += 1
    elif nums[start] + nums[end] < x:
        start += 1
    else:
        end -= 1
print(ans)
