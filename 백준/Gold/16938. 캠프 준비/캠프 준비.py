from itertools import combinations
N, L, R, X = map(int, input().split())
problem = list(map(int, input().split()))
ans = 0
for i in range(2, N+1):
    for combi in combinations(problem, i):
        combi = list(combi)
        # print(combi)
        total = sum(combi)
        # print(total)
        if (max(combi) - min(combi)) >= X and L <= total <= R:
            ans += 1
print(ans)
