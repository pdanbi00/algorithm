# 가중치가 음수도 있으니깐 다익스트라는 안됨
# 벨만 포드 알고리즘
def bf(start):
    dist[start] = 0

    # N번 검사
    for i in range(1, N+1):
        for s in range(1, N+1):
            for next, time in graph[s]:
                if dist[next] > dist[s] + time:
                    dist[next] = dist[s] + time
                    # 음의 사이클 존재
                    if i == N:
                        return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dist = [1e9] * (N+1)
    for i in range(M):
        v1, v2, w = map(int, input().split())
        graph[v1].append((v2, w))
        graph[v2].append((v1, w))
    for j in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))
    negative_cycle_exist = bf(1)
    if negative_cycle_exist:
        print("YES")
    else:
        print("NO")