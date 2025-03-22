import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M = map(int, input().split())
degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split()) # a를 b보다 먼저 풀어야 됨.
    degree[b] += 1
    graph[a].append(b)

q = []

for i in range(1, N+1):
    if degree[i] == 0:
        heappush(q, i)

while q:
    now = heappop(q)
    print(now, end = ' ')
    for next in graph[now]:
        degree[next] -= 1

        if degree[next] == 0:
            heappush(q, next)