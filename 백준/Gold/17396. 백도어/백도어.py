from heapq import heappush, heappop
from sys import stdin, maxsize
input = stdin.readline

N, M = map(int, input().split())
sight = list(map(int, input().split()))

graph = [[] for _ in range(N)]

def dijkstra(start):
    pq = []
    distance = [maxsize] * N
    distance[start] = 0
    heappush(pq, (0, start))

    while pq:
        dis, cur = heappop(pq)

        if distance[cur] < dis:
            continue

        for next_idx, next_d in graph[cur]:
            if distance[next_idx] > distance[cur] + next_d:
                distance[next_idx] = distance[cur] + next_d
                heappush(pq, (distance[next_idx], next_idx))


    return distance

for _ in range(M):
    a, b, t = map(int, input().split())
    if (a != N-1 and sight[a] == 1) or (b != N-1 and sight[b] == 1):
        continue
    graph[a].append((b, t))
    graph[b].append((a, t))

result = dijkstra(0)
# print(result)

if result[N-1] == maxsize:
    print(-1)
else:
    print(result[N-1])