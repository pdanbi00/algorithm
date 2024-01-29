from collections import deque
N, M, V = map(int, input().split())
relations = [[] for _ in range(N+1)]
dfs_visited = [False] * (N+1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    relations[v1].append(v2)
    relations[v2].append(v1)
for i in range(1, N+1):
    relations[i].sort()

def dfs(index):
    dfs_visited[index] = True
    print(index, end=' ')
    for next in relations[index]:
        if not dfs_visited[next]:
            dfs(next)

def bfs(index):
    visited = [False] * (N+1)
    q = deque()
    q.append(index)
    visited[index] = True
    while q:
        a = q.popleft()
        print(a, end=' ')
        for next in relations[a]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

dfs(V)
print()
bfs(V)