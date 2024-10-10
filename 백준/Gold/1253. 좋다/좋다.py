N = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
for i in range(N):
    target = nums[i]
    tmp = nums[:i] + nums[i+1:]
    start = 0
    end = len(tmp)-1
    while start < end:
        if tmp[start] + tmp[end] == target:
            ans += 1
            break
        elif tmp[start] + tmp[end] > target:
            end -= 1
        elif tmp[start] + tmp[end] < target:
            start += 1

print(ans)