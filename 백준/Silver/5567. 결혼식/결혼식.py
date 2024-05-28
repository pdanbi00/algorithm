# bfs 돌려서 visited에 2까지인 애들만 초대
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
ans = 0
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (N+1)
q = deque()
q.append(1)
visited[1] = 0
while q:
    now = q.popleft()
    if visited[now] == 2:
        break
    for next in graph[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
            if visited[next] == 1 or visited[next] == 2:
                ans += 1
print(ans)
