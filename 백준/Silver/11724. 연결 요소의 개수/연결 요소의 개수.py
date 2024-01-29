import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
visited = [False] * (N)
cnt = 0
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1-1].append(v2-1)
    adj[v2-1].append(v1-1)

def dfs(index):
    visited[index] = True
    for next in adj[index]:
        if not visited[next]:
            dfs(next)

for i in range(N):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)