import heapq

def dijkstra(s):
    D = [1e9] * (N+1)
    D[s] = 0
    q = []
    heapq.heappush(q, (0, s)) # heap에 (가중치, 노드) 형식으로 삽입. 앞에 값부터 기준으로 잡고 비교하기 때문에
    while q:
        w, n = heapq.heappop(q) # 최소힙이니깐 가중치가 제일 작은게 pop 될거임
        if D[n] >= w: # 이미 최소값을 구했는지 확인. 가중치 업데이트 된거만 보기 위해서
            for v, val in graph[n]:
                if w+val < D[v]:
                    D[v] = w+val
                    heapq.heappush(q, (D[v], v))
    return D

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2, weight = map(int, input().split())
    graph[v1].append((v2, weight))
ans = dijkstra(X)
ans[0] = 0
for i in range(1, N+1):
    if i != X:
        res = dijkstra(i)
        ans[i] += res[X]
print(max(ans))