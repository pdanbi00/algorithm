import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()
visited = [0] * (N+1)
cnt = 1

def dfs(node):
    global cnt
    for next_node in graph[node]:
        if visited[next_node] == 0:
            cnt += 1
            visited[next_node] = cnt
            dfs(next_node)

visited[R] = 1
dfs(R)
for i in range(1, N+1):
    print(visited[i])
'''
5 6 1
1 4
1 2
2 3
2 4
3 4
5 1
'''