from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
cards = []
ans = 0
for _ in range(N):
    card = int(input())
    heappush(cards, card)

while len(cards) >= 2:
    a = heappop(cards)
    b = heappop(cards)
    tmp = a + b
    ans += tmp
    heappush(cards, tmp)

print(ans)