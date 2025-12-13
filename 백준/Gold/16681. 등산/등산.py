from heapq import heappush, heappop
from sys import stdin, maxsize
input = stdin.readline

def dijkstra(start):
    pq = []
    dist = [INF] * (N+1)
    dist[start] = 0
    heappush(pq, (0, start))

    while pq:
        d, cur = heappop(pq)

        if dist[cur] < d:
            continue

        for next, next_d in graph[cur]:
            # 높아지는 방향으로만
            if heights[next] <= heights[cur]:
                continue

            if dist[next] > dist[cur] + next_d:
                dist[next] = dist[cur] + next_d
                heappush(pq, (dist[next], next))

    return dist

N, M, D, E = map(int, input().split())

heights = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
INF = maxsize


for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist_go = dijkstra(1)
dist_back = dijkstra(N)

answer = -INF

for i in range(2, N):
    if dist_go[i] == INF or dist_back[i] == INF:
        continue

    tmp = (heights[i] * E) - ((dist_go[i] + dist_back[i]) * D)
    answer = max(answer, tmp)

if answer == -INF:
    print("Impossible")
else:
    print(answer)