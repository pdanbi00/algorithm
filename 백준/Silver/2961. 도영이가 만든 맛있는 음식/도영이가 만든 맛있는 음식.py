from itertools import combinations
N = int(input())
food = []
for _ in range(N):
    sour, bitter = map(int, input().split())
    food.append((sour, bitter))

ans = 1000000000
for i in range(1, N+1):
    for comb in combinations(food, i):
        s, b = 1, 0
        for sour, bitter in comb:
            s *= sour
            b += bitter
        ans = min(ans, abs(s - b))

print(ans)