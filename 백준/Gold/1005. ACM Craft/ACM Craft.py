from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    buildings = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)] # 각 건물을 짓게 위해 미리 지어져야하는 건물들 정보
    inDegree = [0] * (N+1)
    dp = [0] * (N + 1)
    q = deque()

    for i in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1
    W = int(input())

    for i in range(1, N+1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = buildings[i]

    while q:
        tmp = q.popleft()

        for next in graph[tmp]:
            inDegree[next] -= 1
            dp[next] = max(dp[next], dp[tmp] + buildings[next])
            if inDegree[next] == 0:
                q.append(next)

    print(dp[W])