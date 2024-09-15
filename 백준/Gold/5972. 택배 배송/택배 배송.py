# 다익스트라
from heapq import heappush, heappop

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

costs = [1e9] * (N+1)
heap = []

start = 1
end = N

costs[start] = 0
heappush(heap, [0, start])

while heap:
    cur_cost, cur_v = heappop(heap)

    if costs[cur_v] >= cur_cost:
        for next_v, next_cost in graph[cur_v]:
            sum_cost = cur_cost + next_cost
            if sum_cost < costs[next_v]:
                costs[next_v] = sum_cost
                heappush(heap, [costs[next_v], next_v])

print(costs[end])