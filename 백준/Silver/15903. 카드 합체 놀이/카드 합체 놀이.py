import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
heapq.heapify(cards)
for i in range(M):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    a, b = a+b, a+b
    heapq.heappush(cards, a)
    heapq.heappush(cards, b)
for i in range(len(cards)):
    ans += heapq.heappop(cards)
print(ans)
