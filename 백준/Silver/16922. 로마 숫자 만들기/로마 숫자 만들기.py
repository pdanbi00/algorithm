from itertools import combinations_with_replacement
N = int(input())
ans = set()
nums = (1, 5, 10, 50)
for com in combinations_with_replacement(nums, N):
    tmp = sum(com)
    ans.add(tmp)
print(len(ans))
