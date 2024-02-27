# DFS
def dfs(n, cnt):
    global ans
    if n == second:
        ans = cnt
    visited[n] = True
    for next in graph[n]:
        if not visited[next]:
            dfs(next, cnt+1)
ans = -1
N = int(input())
first, second = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
dfs(first, 0)
print(ans)
