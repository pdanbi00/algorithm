from itertools import product

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = set()
for pro in product(nums, repeat=M):
    possible = True
    for i in range(M-1):
        if pro[i] > pro[i+1]:
            possible = False
            break
    if possible:
        ans.add(pro)

ans = list(ans)
ans.sort()
for a in ans:
    print(*a)