from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

X = int(input())

visited = [False] * (N+1)

visited[X] = True
q = deque()
q.append(X)

while q:
    cur = q.popleft()

    for k in graph[cur]:
        if not visited[k]:
            q.append(k)
            visited[k] = True

print(sum(visited)-1)