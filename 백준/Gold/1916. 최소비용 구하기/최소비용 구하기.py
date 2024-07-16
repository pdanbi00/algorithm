from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

board = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    board[a].append((b, cost))

start, end = map(int, input().split())
# 다익스트라

cost = [1e9] * (N+1)
heap = []

cost[start] = 0
heappush(heap, [0, start])

while heap:
    cur_cost, cur_v = heappop(heap)
    if cost[cur_v] >= cur_cost:
        for next_v, next_cost in board[cur_v]:
            sum_cost = cur_cost + next_cost
            if sum_cost < cost[next_v]:
                cost[next_v] = sum_cost
                heappush(heap, [sum_cost, next_v])
print(cost[end])

