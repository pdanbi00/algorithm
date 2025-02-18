import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [-1] * (N+1)

def dfs(node):
    global visited
    visited[node] = 1
    for next_node in graph[node]:
        if visited[next_node] == -1:
            visited[node] += dfs(next_node)
    return visited[node]

dfs(R)
for _ in range(Q):
    U = int(input())
    print(visited[U])