# 가장 빠른 시간? BFS
from collections import deque
N, K = map(int, input().split())
visited = [0] * 200001
q = deque()
q.append(N)
visited[N] = 0
while q:
    now = q.popleft()
    if now == K:
        print(visited[now])
        break
    if now - 1 >= 0 and visited[now-1] == 0:
        q.append(now-1)
        visited[now-1] = visited[now] + 1
    if now + 1 <= 200000 and visited[now+1] == 0:
        q.append(now+1)
        visited[now+1] = visited[now] + 1
    if now * 2 <= 200000 and visited[now*2] == 0:
        q.append((now*2))
        visited[now*2] = visited[now] + 1
