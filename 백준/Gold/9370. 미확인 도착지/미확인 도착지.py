from heapq import heappush, heappop
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dijkstra(start):
    q = []
    # 최단거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n+1)
    # 시작노드로 가기 위한 최단 경로는 0으로 설정하고 큐에 삽입
    distance[start] = 0
    heappush(q, (0, start))

    while q:
        # 가장 거리가 짧은 노드 가져오기
        dis, node = heappop(q)
        # 현재 노드가 처리된 노드라면 패스
        if distance[node] < dis:
            continue

        # 현재 노드와 연결된 다른 인접한 노드 확인
        for next_node in graph[node]:
            cost = dis + next_node[1]
            # 현재 노드를 거쳐서 가는게 거리가 더 짧을 경우
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heappush(q, (cost, next_node[0]))
    return distance

    pass

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split()) # 교차로 수, 도로 수, 목적지 후보 개수
    s, g, h = map(int, input().split()) # 출발지, g, h
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    target = [int(input()) for _ in range(t)]

    # s랑 g 사이의 최소거리
    # g랑 target들 사이의 최소거리
    # s랑 h 사이의 최소거리
    # h랑 target들 사이의 최소거리

    # 다익스트라
    first = dijkstra(s)

    g_dijkstra = dijkstra(g)
    h_dijkstra = dijkstra(h)

    arr = []
    for tg in target:
        if first[g] + g_dijkstra[h] + h_dijkstra[tg] == first[tg] or first[h] + h_dijkstra[g] + g_dijkstra[tg] == first[tg]:
            arr.append(tg)

    arr.sort()
    print(*arr)
