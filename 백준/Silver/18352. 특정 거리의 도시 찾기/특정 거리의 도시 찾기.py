from collections import deque
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (N+1)
q = deque()
q.append(X)
visited[X] = 0
ans = []
while q:
    now = q.popleft()
    if visited[now] == K:
        ans.append(now)

    for next in graph[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1

if ans:
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])
else:
    print(-1)