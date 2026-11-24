from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort(reverse=True)

visited = [0] * (N+1)
q = deque()
q.append(R)
visited[R] = 1
cnt = 1

while q:
    cur = q.popleft()

    for k in graph[cur]:
        if visited[k] == 0:
            q.append(k)
            visited[k] = cnt + 1
            cnt += 1

for i in range(1, N+1):
    print(visited[i])