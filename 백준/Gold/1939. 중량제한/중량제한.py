from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, N+1):
    graph[i].sort(reverse=True)

distance = [0] * (N+1)
start, end = map(int, input().split())


def dijkstra(v1, v2):
    global ans
    q = []
    heappush(q, (0, v1))

    for next_node, cost in graph[v1]:
        distance[next_node] = cost
        heappush(q, (-cost, next_node))

    while q:
        dist, v = heappop(q)
        dist = -1 * dist

        if v == v2:
            print(dist)
            break

        if distance[v] > dist:  # 이미 최대 중량일 경우 패스
            continue

        for next_node, cost in graph[v]:
            if distance[next_node] < dist and distance[next_node] < cost:
                distance[next_node] = min(dist, cost)
                heappush(q, (-distance[next_node], next_node))

dijkstra(start, end)