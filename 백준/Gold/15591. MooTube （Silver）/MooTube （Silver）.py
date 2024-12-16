from collections import deque
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(N-1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

for _ in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N+1)
    visited[v] = True
    result = 0
    q = deque()
    q.append((v, 1e9))
    while q:
        node, usado = q.popleft()
        for next_node, next_usado in graph[node]:
            next_usado = min(next_usado, usado)
            if next_usado >= k and not visited[next_node]:
                result += 1
                q.append((next_node, next_usado))
                visited[next_node] = True
    print(result)