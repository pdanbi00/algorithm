from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[b].append(a)
find = False

def dfs(node):
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)

for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[0] = True
    visited[i] = True
    dfs(i)
    if False not in visited:
        answer = i
        find = True
        break

if find:
    print(answer)
else:
    print(-1)