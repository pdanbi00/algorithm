from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    buildings = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)] # 각 건물을 짓게 위해 미리 지어져야하는 건물들 정보
    for i in range(K):
        a, b = map(int, input().split())
        graph[b].append(a)
    W = int(input())

    q = deque()
    for i in range(1, N+1):
        q.append(i)
    dp = [-1] * (N+1)

    while q:
        now = q.popleft()
        possible = True
        for next in graph[now]:
            if dp[next] == -1:
                possible = False
                q.append(now)
                break
        if possible:
            dp[now] = buildings[now]
            for next in graph[now]:
                dp[now] = max(dp[now], dp[next] + buildings[now])

    print(dp[W])
