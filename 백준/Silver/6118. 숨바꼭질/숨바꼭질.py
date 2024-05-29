import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans_number = 0
ans_dist = 0
ans_cnt = 0
q = deque()
q.append(1)
visited = [-1] * (N+1)
visited[1] = 0
while q:
    now = q.popleft()
    for next in graph[now]:
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
ans_dist = max(visited)
for i in range(1, N+1):
    if visited[i] == ans_dist:
        if ans_cnt == 0:
            ans_number = i
        ans_cnt += 1
print(ans_number, ans_dist, ans_cnt)