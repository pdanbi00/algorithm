import sys, collections
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
result = collections.Counter(nums).most_common(n=1)[0][1]
nums = sorted({*nums})
N = len(nums)

index = {nums[i]: i for i in range(N)}
visited = [[0] * N for _ in range(N)]

for i in range(N-result):
    for j in range(i+1, N):
        if visited[i][j]:
            continue
        diff, l = nums[j] - nums[i], 2
        while index.get(nums[j] + diff):
            k = index[nums[j] + diff]
            visited[j][k] = 1
            l += 1
            j = k
        result = max(result, l)

print(result)