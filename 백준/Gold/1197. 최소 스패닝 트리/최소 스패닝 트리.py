# prim
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [0] * (V+1)
ans = 0

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

q = [(0, 1)]

def prim():
    global ans
    while q:
        weight, node = heappop(q)
        if visited[node] == 0:
            visited[node] = 1
            ans += weight
            for next_weight, next_node in graph[node]:
                heappush(q, (next_weight, next_node))
prim()
print(ans)
