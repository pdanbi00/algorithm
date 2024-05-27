import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
member = [0] * (N+1)
graph = [[] for _ in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

# 각 점으로 가는 최소 이동거리를 구해서 그 max 값이 가장 작은게 회장 후보가 됨
def bfs(idx):
    visited = [-1] * (N+1)
    visited[idx] = 0
    q = deque()
    q.append(idx)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[now] + 1
    return max(visited)
ans = 50
for i in range(1, N+1):
    tmp = bfs(i)
    if tmp < ans:
        ans = tmp
        ans_mem = [i]
    elif tmp == ans:
        ans_mem.append(i)
print(ans, len(ans_mem))
print(*ans_mem)