from heapq import heappush, heappop


# 다익스트라
# 1번 마을에서 나머지 모든 마을까지의 최단거리를 구하고 K이하인 마을 개수 세기
def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N+1)]
    for i in range(len(road)):
        a, b, d = road[i][0], road[i][1], road[i][2]
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    distance = [1e9] * (N+1)
    distance[1] = 0
    
    q = []
    heappush(q, (0, 1))
    
    while q:
        dis, node = heappop(q)
        if dis > distance[node]:
            continue
            
        for n, d in graph[node]:
            if dis + d <= distance[n]:
                distance[n] = dis+d
                heappush(q, (distance[n], n))
    
    # print(distance)
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1    

    return answer