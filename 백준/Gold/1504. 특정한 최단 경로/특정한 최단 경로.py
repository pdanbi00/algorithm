# 방법 : 시작 정점(1) -> v1 -> v2 -> 끝 정점(N)
#       시작 정점(1) -> v2 -> v1 -> 끝 정점(N)
# 다익스트라 : 모든 정점을 다 경유지로 고려해서 최종적으로 출발지에서 모든 정점으로의 최단 경로를 구하는 알고리즘
# 동작 과정:
# 1. 출발지점을 정한다.
# 2. 최단 거리 테이블 초기화
# 3. 현재 노드와 연결된 노드 중 방문하지 않았고, 거리가 가장 짧은 노드 선택
# 4. 선택한 노드와 연결된 노드 중 방문하지 않은 노드에 대해 기존의 가중치와, 해당 노드를 거치는 경우의 가중치와 비교해서 최단거리 테이블을 갱신
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, input().split())

def dijkstra(s, e):
    D = [1e9] * (N+1)
    D[s] = 0
    q = []
    heappush(q, (0, s))
    while q:
        w, n = heappop(q)
        if w > D[n]:
            continue
        for next_node, weight in graph[n]:
            if D[next_node] > D[n] + weight:
                D[next_node] = D[n] + weight
                heappush(q, (D[next_node], next_node))
    return D[e]

# 1 -> v1 -> v2 -> N
path1 = dijkstra(1, start) + dijkstra(start, end) + dijkstra(end, N)

# 1 -> v2 -> v1 -> N
path2 = dijkstra(1, end) + dijkstra(end, start) + dijkstra(start, N)

if path1 >= 1e9 and path2 >= 1e9:
    print(-1)
else:
    print(min(path1, path2))
