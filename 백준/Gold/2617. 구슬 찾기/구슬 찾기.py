# 가벼운거 -> 무거운거, 무거운거 -> 가벼운거 bfs 돌면서
# 모든 구슬에서 다 돌면서 개수 확인
from collections import deque
N, M = map(int, input().split())
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
ans = 0

def bfs(idx, graph):
    q = deque()
    q.append(idx)
    visited = [-1] * (N+1)
    visited[idx] = 0
    cnt = 0
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[now] + 1
                cnt += 1
    return cnt

for _ in range(M):
    a, b = map(int, input().split())
    graph1[b].append(a)
    graph2[a].append(b)

for i in range(1, N+1):
    tmp1 = bfs(i, graph1)
    tmp2 = bfs(i, graph2)
    if tmp1 >= (N // 2) + 1 or tmp2 >= (N // 2) + 1:
        ans += 1
print(ans)