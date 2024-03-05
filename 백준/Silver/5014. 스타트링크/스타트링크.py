# BFS
from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [-1] * (F+1)
find = False
q = deque()
q.append(S)
visited[S] = 0
while q:
    now = q.popleft()
    if now == G:
        find = True

    next = now + U
    if 1 <= next <= F and visited[next] == -1:
        q.append(next)
        visited[next] = visited[now] + 1
    next = now - D
    if 1 <= next <= F and visited[next] == -1:
        q.append(next)
        visited[next] = visited[now] + 1
if find:
    print(visited[G])
else:
    print("use the stairs")