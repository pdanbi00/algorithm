# 다익스트라
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
for i in range(1, V+1):
    graph[i].sort(key=lambda x: x[1])

def dijkstra(s):
    D = [1e9] * (V+1)
    D[s] = 0
    q = []
    heappush(q, (0, s))
    while q:
        weight, node = heappop(q)
        if D[node] >= weight:
            for next_node, w in graph[node]:
                if D[next_node] > D[node] + w:
                    D[next_node] = D[node] + w
                    heappush(q, (D[next_node], next_node))
    return D
result = dijkstra(start)
for i in range(1, V+1):
    if result[i] == 1e9:
        print("INF")
    else:
        print(result[i])