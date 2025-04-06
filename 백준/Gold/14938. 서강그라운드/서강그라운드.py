# 각 점에서의 최단 거리를 모두 구하고
# 최단거리가 수색 범위 이내인 경우 아이템 개수 다 더해서 갱신학
from heapq import heappush, heappop
N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(i):
    distance = [1e9] * (N + 1)
    distance[i] = 0
    heap = []
    heappush(heap, (0, i))
    while heap:
        cur_dis, cur_r = heappop(heap)
        if distance[cur_r] < cur_dis:
            continue
            
        for next_r, next_dis in graph[cur_r]:
            dis = cur_dis + next_dis
            if dis < distance[next_r]:
                heappush(heap, (dis, next_r))
                distance[next_r] = dis
    return distance

ans = 0
# i에서 각 점까지의 최단거리 구하기
for i in range(1, N+1):
    arr = dijkstra(i)
    tmp = 0
    for k in range(1, N+1):
        if arr[k] <= M:
            tmp += items[k]
    ans = max(ans, tmp)

print(ans)