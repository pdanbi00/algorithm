import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

X = int(input())

# finished = set()
visited = [0] * (N+1)
visited[X] = 1

def dfs(cur):
    for k in graph[cur]:
        if not visited[k]:
            visited[k] = True
            dfs(k)


dfs(X)
print(sum(visited)-1)