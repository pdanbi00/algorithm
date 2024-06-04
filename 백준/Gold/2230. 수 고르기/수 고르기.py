import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)
nums.sort()
start = 0
end = 0
ans = nums[-1] * 2

while start <= end and end < N:
    if nums[end] - nums[start] >= M:
        if ans > nums[end] - nums[start]:
            ans = nums[end] - nums[start]
        start += 1
    else:
        end += 1
print(ans)