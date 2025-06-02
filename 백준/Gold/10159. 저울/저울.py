# 플로이드와샬

INF = int(1e9)
N = int(input())
M = int(input())

graph = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신으로 돌아가는 노드 비용은 0으로 초기화
for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

# a에서 b로 가는 경로가 있는지 확인하기 (플로이드와샬)
for k in range(1, N+1):
    for a in range(1, N+1): # 출발노드
        for b in range(1, N+1): # 도착노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# a, b 비교 가능한지 확인
for a in range(1, N+1):
    cnt = 0
    for b in range(1, N+1):
        if graph[a][b] == INF and graph[b][a] == INF: # a > b, b > a인 경로가 없는 경우
            cnt += 1

    print(cnt)