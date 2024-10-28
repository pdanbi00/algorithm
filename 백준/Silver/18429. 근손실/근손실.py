from itertools import permutations

N, K = map(int, input().split())
kit = list(map(int, input().split()))
cnt = 0
for perm in permutations(kit):
    weight = 500
    possible = True
    for i in range(N):
        weight += perm[i]
        weight -= K
        if weight < 500:
            possible = False
            break
    if possible:
        cnt += 1
print(cnt)
