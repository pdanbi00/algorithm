from collections import deque
V = int(input())
graph = [[] for _ in range(V+1)]
# 2차원 리스트에 트리 저장(연결리스트)
for i in range(V):
    line = list(map(int, input().split()))
    node_cnt = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        graph[node_cnt].append((adj_node, adj_cost))
        idx += 2

visited = [-1] * (V+1)
visited[1] = 0

# visited에 모든 노드까지의 거리 저장
def DFS(node, dist):
    for v, d in graph[node]:
        cal_dist = dist + d
        if visited[v] == -1:
            visited[v] = cal_dist
            DFS(v, cal_dist)
    return

# 1. 아무 노드에서 제일 멀리 떨어진 노드를 찾는다
# 2. 그 노드에서 제일 멀리 떨어진 노드 사이의 거리가 트리의 지름이 됨
# 그래서 아무노드 1에서 제일 멀리 떨어진걸 찾기 위해 DFS(1, 0) 함
# DFS(2, 0) 해도 답 똑같이 나옴.(15번째 줄에 vistied[2] = 0 해줘야 됨.)
DFS(1, 0)
tmp = [0, 0]
# 최대 거리에 있는 노드 찾기
for i in range(1, len(visited)):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i

# 찾은 노드와, 찾은 노드에서 DFS 돌렸을때 최대거리 노드가 지름의 양 끝점
# 논리 : 임의의 노드에서 최대 거리에 있는 노드는 반드시 트리의 지름의 양 끝점 중 하나이다.
visited = [-1] * (V+1)
visited[tmp[0]] = 0
DFS(tmp[0], 0)

print(max(visited))
