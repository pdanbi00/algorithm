# BFS
# 더미 스테이션을 추가로 만들어서
# 더미 스테이션에 역들을 연결
# 각 튜브를 임의의 더미 스테이션으로 정해서 스테이션에 해당 튜브에 연결된 역들 연결

import sys
input = sys.stdin.readline

from collections import deque

N, K, M = map(int, input().split())
graph = [[] for _ in range(N+M+1)] # 역 개수 N+1개 + 튜브개수 M개

for i in range(1, M+1):
    tube = list(map(int, input().split()))
    for j in range(K):
        graph[tube[j]].append(N+i)
        graph[N+i].append(tube[j])

q = deque()
q.append(1)
visited = [-1] * (N+M+1)
visited[1] = 1
while q:
    now = q.popleft()
    for next in graph[now]:
        if visited[next] == -1:
            if next > N: # 더미 스테이션일 경우 횟수 추가 안함.
                q.append(next)
                visited[next] = visited[now]
            else: # 일반 역일 경우 횟수 추가
                q.append(next)
                visited[next] = visited[now] + 1
print(visited[N])
