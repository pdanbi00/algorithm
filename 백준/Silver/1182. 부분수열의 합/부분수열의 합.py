from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    for com in combinations(nums, i):
        if sum(com) == S:
            cnt += 1

print(cnt)