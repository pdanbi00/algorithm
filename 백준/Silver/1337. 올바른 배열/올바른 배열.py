N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

ans = 5
nums.sort()

if N < 5:
    for i in range(N):
        cnt = 0
        for j in range(5):
            if nums[i] + j in nums:
                cnt += 1
        ans = min(ans, 5-cnt)
else:
    for i in range(N):
        cnt = 0
        for j in range(5):
            if nums[i] + j in nums:
                cnt += 1
        ans = min(ans, 5-cnt)

print(ans)