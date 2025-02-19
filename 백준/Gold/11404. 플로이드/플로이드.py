n = int(input())
m = int(input())
graph = [[1e9] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b]) # 시작 도시와 도착 도시를 연결하는 노선이 하나가 아닐 수 있어서.

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
           graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 1e9:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()
