# 이것은 dfs이올시다
import sys
sys.setrecursionlimit(10000)
def dfs(n):
    for k in range(N):
        if graph[n][k] == 1 and visited[k] == 0:
            visited[k] = 1 # 방문 표시랑 dfs 재귀 호출 순서가 중요
            dfs(k)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = [[0]*N for _ in range(N)]
for i in range(N):
    visited = [0] * N
    dfs(i)
    for j in range(N):
        if visited[j]:
            ans[i][j] = 1

for i in range(N):
    print(*ans[i])