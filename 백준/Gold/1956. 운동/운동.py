# 플로이드 워샬 : 경유지 기준으로 경유지를 들렀을 경우와 아닌 경우를 비교하면서 최소 비용 루트를 찾는 방법
# 자기 자신에서 자기 자신으로 돌아오는 거리 중에 최솟값 구하기

# A에서 B로 가는 최단거리랑, A에서 k를 거쳐서 B로 가는 거리를 비교하는 방식
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
# 거리를 담는 그래프
graph = [[int(1e9)] * (V) for _ in range(V)]
for _ in range(E):
    v1, v2, dis = map(int, input().split())
    graph[v1-1][v2-1] = dis

# 1. 모든 정덤에서 모든 정점으로 가는 최소 거리 구하기기
# 경유지 k, 출발지 i, 도착지 j로 3중 for문 돌기
for k in range(V):
    for i in range(V):
        for j in range(V):
            # i -> j가 빠른지 i -> k -> j가 빠른지 검사
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 2. 자기자신에서 자기자신으로 돌아오는 거리 중 최소 값 구하기
ans = 1e9
for i in range(V):
    if graph[i][i] < ans:
      ans = graph[i][i]

if ans == 1e9:
    print(-1)
else:
    print(ans)
