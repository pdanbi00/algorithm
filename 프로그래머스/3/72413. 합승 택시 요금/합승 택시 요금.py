from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    INF = 100000000000
    # 다익스트라로 구현
    graph = [[] for _ in range(n+1)]

    for v1, v2, p in fares:
        graph[v1].append((v2, p))
        graph[v2].append((v1, p))
        
    # 다익스트라 알고리즘
    def dijkstra(start):
        distance = [INF] * (n+1)
        distance[start] = 0
        q = []
        heappush(q, (0, start))
        
        while q:
            cur_dist, cur_node = heappop(q)
            
            if distance[cur_node] < cur_dist:
                continue
            
            for next_node, next_dist in graph[cur_node]:
                if distance[next_node] > cur_dist + next_dist:
                    distance[next_node] = cur_dist + next_dist
                    heappush(q, (distance[next_node], next_node))
        return distance
    
    # 우리가 구하고자 하는 최소 거리비용 : 출발점에서 특정 노드까지의 거리 + 특정 노드에서 a까지의 거리 + 특정 노드에서 b까지의 거리
    # 출발점이랑 특정노드가 같다면 혼자 택시를 탑승하는 경우
    # 출발점이랑 특정노드가 다르다면 출발점에서 특정노드까지는 합승해서 이용
    dist = [[]]
    ans = INF
    for i in range(1, n+1):
        dist.append(dijkstra(i))
    for i in range(1, n+1):
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])
    return ans