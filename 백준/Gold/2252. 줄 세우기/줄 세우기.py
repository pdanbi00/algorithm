# 위상정렬
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
degree = [0] * (N+1)
graph = [[] for  _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    degree[b] += 1
    graph[a].append(b)

q = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)
answer = []

while q:
    tmp = q.popleft()
    answer.append(tmp)
    for next_tmp in graph[tmp]:
        degree[next_tmp] -= 1
        if degree[next_tmp] == 0:
            q.append(next_tmp)
print(*answer)