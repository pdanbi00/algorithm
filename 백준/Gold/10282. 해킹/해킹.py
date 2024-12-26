# 다익스트라
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start, dp, graph):
    heappush(heap, [0, start])
    dp[start] = 0
    while heap:
        w, n = heappop(heap)
        for next_n, weight in graph[n]:
            next_weight = w + weight
            if next_weight < dp[next_n]:
                dp[next_n] = next_weight
                heappush(heap, [next_weight, next_n])

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dp = [1e9] * (n+1)
    heap = []
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    dijkstra(c, dp, graph)

    cnt = 0
    time = 0
    for i in dp:
        if i != 1e9:
            cnt += 1
            time = max(time, i)
    print(cnt, time)