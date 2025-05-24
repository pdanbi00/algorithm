# 다익스트라
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((i, b))
    graph[b].append((i, a))

def dijkstra():
    q = []
    heappush(q, (0, 1))
    visited = [INF] * (N+1)
    visited[1] = 0

    while q:
        time, node = heappop(q)
        if node == N:
            return time

        if visited[node] < time:
            continue

        for i, nnode in graph[node]:
            if (time-i) % M == 0:
                ntime = i + ((time-i) // M) * M
            else:
                ntime = i + ((time-i) // M + 1) * M

            if visited[nnode] > ntime + 1:
                visited[nnode] = ntime + 1
                heappush(q, (ntime+1, nnode))

print(dijkstra())