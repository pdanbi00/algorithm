import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
heapq.heapify(cards)
for i in range(M):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    heapq.heappush(cards, a+b)
    heapq.heappush(cards, a+b)

print(sum(cards))