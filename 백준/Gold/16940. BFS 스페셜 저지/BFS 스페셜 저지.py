from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
children = [set() for _ in range(N+1)] # 트리의 부모자식 관계를 알기 위ㅎ해서
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
path = list(map(int, input().split()))

# BFS
q = deque()
q.append(1)
visited[1] = 1
while q:
    now = q.popleft()
    for node in graph[now]:
        if visited[node] == -1:
            q.append(node)
            visited[node] = visited[now] + 1
            children[now].add(node)

next_idx = 1
for i in path:
    # print(i)
    if next_idx == N:
        break
    length = len(children[i]) # 자식 길이
    # print('children : ', children[i])
    c1 = set(path[next_idx:next_idx + length])
    # print('c1 : ', c1)
    c2 = children[i]
    # print('c2 : ', c2)
    if c1 != c2:
        print(0)
        exit()
    next_idx += length
print(1)