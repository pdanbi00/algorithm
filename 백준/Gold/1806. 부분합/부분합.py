N, S = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(1, N):
    nums[i] += nums[i-1]

ans = 100000
start = 0
end = 0

while end < N:
    if start == 0:
        tmp = nums[end]
    else:
        tmp = nums[end] - nums[start-1]
    if tmp >= S:
        ans = min(ans, end-start+1)
        start += 1
    else:
        end += 1
if ans == 100000:
    print(0)
else:
    print(ans)
