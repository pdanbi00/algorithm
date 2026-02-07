from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
info = []

for _ in range(N):
    p, d = map(int, input().split())
    info.append((p, d))

info.sort(key=lambda x : (x[1], -x[0]))

pq = []
for pay, day in info:
    heappush(pq, pay)
    if day < len(pq):
        heappop(pq)

print(sum(pq))