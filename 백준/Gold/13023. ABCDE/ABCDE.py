import sys
N, M = map(int, input().split())
edges = [] # 간선리스트
a = [[False] * N for _ in range(N)] # 인접행렬 - a[i][j] : i번 노드랑 j번 노드랑 연결되어 있다.
g = [[] for _ in range(N)] # 인접 리스트 - a[i] : i번 노드랑 연결된 모든 노드들 정보가 들어있음
for _ in range(M):
    v1, v2 = map(int, input().split())
    edges.append((v1, v2))
    edges.append((v2, v1))
    a[v1][v2] = True
    a[v2][v1] = True
    g[v1].append(v2)
    g[v2].append(v1)

M *= 2 # 양쪽 노드 모두에 간선정보 담았으니깐 2배해줌
for i in range(M):
    for j in range(M):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not a[B][C]:
            continue
        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit(0)
print(0)