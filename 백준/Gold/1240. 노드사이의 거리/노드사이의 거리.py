from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
distance = [[1e9] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    visited = [False] * (N+1)
    q = deque()
    q.append((a, 0))
    visited[a] = True
    while q:
        next, dis = q.popleft()
        if next == b:
            print(dis)
        else:
            for k, w in graph[next]:
                if not visited[k]:
                    q.append((k, dis + w))
                    visited[k] = True