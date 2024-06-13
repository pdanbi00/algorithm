N, S = map(int, input().split())
nums = list(map(int, input().split()))

ans = 100000
start = 0
end = 0
tmp = 0

while True:
    if tmp >= S:
        ans = min(ans, end-start)
        tmp -= nums[start]
        start += 1
    elif end == N:
        break
    else:
        tmp += nums[end]
        end += 1
if ans == 100000:
    print(0)
else:
    print(ans)
