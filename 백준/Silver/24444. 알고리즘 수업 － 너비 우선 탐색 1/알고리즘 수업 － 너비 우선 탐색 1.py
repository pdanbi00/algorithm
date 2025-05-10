from collections import deque
import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(N+1):
    graph[i].sort()

visited = [0] * (N+1)
idx = 1
q = deque()
q.append(R)
visited[R] = idx
while q:
    node = q.popleft()
    for next_node in graph[node]:
        if visited[next_node] == 0:
            idx += 1
            q.append(next_node)
            visited[next_node] = idx

for i in range(1, N+1):
    print(visited[i])
