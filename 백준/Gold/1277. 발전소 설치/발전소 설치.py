from heapq import heappush, heappop
from math import sqrt

N, W = map(int, input().split())
M = float(input())

power = []
graph = [[1e9] * (N) for _ in range(N)]
for i in range(N):
    x, y = map(int, input().split())
    power.append([x, y])

def distance(x1, y1, x2, y2):
    return sqrt((x2-x1) ** 2 + (y2-y1) ** 2)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        graph[i][j] = distance(power[i][0], power[i][1], power[j][0], power[j][1])
        # 거리가 M보다 멀면 max값으로
        if graph[i][j] > M:
            graph[i][j] = 1e9

for _ in range(W):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 0
    graph[b-1][a-1] = 0

# 다익스트라
dis = [1e9] * N
dis[0] = 0

q = []
heappush(q, (0, 0))

while q:
    dist, node = heappop(q)

    # 방문 확인
    if dis[node] < dist:
        continue

    for i in range(N):
        if graph[node][i] == 1e9: # 거리가 M보다 멀거나 본인으로 가는 경우
            continue

        new_cost = dist + graph[node][i]
        if new_cost < dis[i]:
            dis[i] = new_cost
            heappush(q, (dis[i], i))

print(int(dis[N-1] * 1000))