import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
dist = [1e9] * (N+1)
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    dist[start] = 0
    nodes[start].append(start)

    while q:
        weight, node = heappop(q)
        # 현재 노드가 이미 처리 됐으면 패스
        if dist[node] < weight:
            continue
        for next_node, next_weight in graph[node]:
            cost = weight + next_weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                nodes[next_node] = nodes[node] + [next_node]
                heappush(q, (cost, next_node))

dijkstra(start)
print(dist[end])
print(len(nodes[end]))
print(*nodes[end])