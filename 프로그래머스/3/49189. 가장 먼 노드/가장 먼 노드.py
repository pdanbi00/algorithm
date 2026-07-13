# 한 노드에서 다른 모든 노드들 사이의 거리를 구하는 것이니깐 최단 경로 알고리즘
# 가중치가 양수니깐 다익스트라

from heapq import heappush, heappop

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [1e9] * (n+1)
    distance[1] = 0
    q = []
    
    for i in range(len(edge)):
        a, b = edge[i][0], edge[i][1]
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    heappush(q, (0, 1))
    
    # dijkstra
    while q:
        dis, node = heappop(q)
        
        if dis > distance[node]:
            continue
        
        for next_node, weight in graph[node]:
            W = dis + weight
            if distance[next_node] > W:
                distance[next_node] = W
                heappush(q, (W, next_node))
    
    # print(distance)
    max_v = -1
    cnt = 0
    for i in range(1, n+1):
        if max_v < distance[i]:
            max_v = distance[i]
            cnt = 1
        elif max_v == distance[i]:
            cnt += 1
    
    return cnt