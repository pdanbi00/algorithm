import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

def dfs(path):
    tmp = path.popleft()
    if not path:
        print(1)
        exit()
    visited[tmp] = 1
    for i in range(len(graph[tmp])):
        if path[0] in graph[tmp] and visited[path[0]] == 0:
            dfs(path)
    return

if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    path = deque(map(int, input().split()))
    
    if path[0] != 1:
        print(0)
    else:
        dfs(path)
        print(0)