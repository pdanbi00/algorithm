from itertools import combinations
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 1e9

for i in range(1, N+1):
    tmp = 0
    if len(graph[i]) >= 2:
        for combi in combinations(graph[i], 2):
            if combi[0] in graph[combi[1]]:
                tmp += len(graph[i]) - 2
                tmp += len(graph[combi[0]]) - 2
                tmp += len(graph[combi[1]]) - 2
                answer = min(answer, tmp)


if answer == 1e9:
    print(-1)
else:
    print(answer)