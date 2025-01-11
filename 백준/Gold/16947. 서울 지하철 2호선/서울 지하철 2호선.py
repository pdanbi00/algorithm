import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# dfs로 사이클 찾기
def dfs(node, cnt):
    # 이미 방문한 노드인데 거리 차이가 3이상이면 사이클
    if check[node]:
        if cnt - dist[node] >= 3:
            return node
        else: return -1
    check[node] = 1
    dist[node] = cnt
    for next_node in adj_list[node]:
        cycleStartNode = dfs(next_node, cnt+1)
        # 시작 정점의 번호라면
        if cycleStartNode != -1:
            check[node] = 2
            # 사이클에 해당하지 않으면 check에 사이클로 기록하지 않기 위해서
            if node == cycleStartNode:
                return -1
            else:
                return cycleStartNode
    return -1

N = int(input())
adj_list = [[] * (N+1) for _ in range(N+1)]
# check[i] = 0 : 방문하지 않은 노드
# check[i] = 1 : 방문한 노드
# check[i] = 2 : 사이클에 속하는 노드
check = [0] * (N+1)
dist = [0] * (N+1)

for _ in range(N):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# 사이클 찾기
dfs(1, 0)

# bfs로 사이클과의 거리 계산
q = deque()
for i in range(1, N+1):
    if check[i] == 2:
        q.append(i)
        dist[i] = 0
    else:
        dist[i] = -1

while q:
    x = q.popleft()
    for y in adj_list[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x] + 1

print(' '.join(map(str, dist[1:])))