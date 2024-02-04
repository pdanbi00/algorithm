from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
for card in combinations(cards, 3):
    total = sum(card)
    if total <= M and total > ans:
        ans = total
print(ans)