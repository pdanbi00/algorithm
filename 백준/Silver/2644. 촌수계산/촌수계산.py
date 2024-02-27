# BFS
from collections import deque
N = int(input())
first, second = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
q = deque()
q.append((first, 0))
visited[first] = True
ans = -1
while q:
    now, cnt = q.popleft()
    if now == second:
        ans = cnt
    for next in graph[now]:
        if not visited[next]:
            q.append((next, cnt + 1))
            visited[next] = True
print(ans)