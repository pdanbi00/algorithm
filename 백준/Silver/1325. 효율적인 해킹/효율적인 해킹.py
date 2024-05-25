import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 노드마다 bfs 돌아서 개수 세서 가장 많은 노드
# A가 B를 신뢰한다 -> B는 A의 부모노드

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 0

    visited = [False] * (N+1)
    visited[start] = True

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1

    return cnt

result = []
for start in range(1, N+1):
    result.append(bfs(start))

for i in range(N):
    if result[i] == max(result):
        print(i+1, end=' ')