N, M = map(int, input().split())
memory = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
answer = sum(costs)
# dp[i][j] : i번째 앱까지 중 j비용으로 얻을 수 있는 최대의 바이트
dp = [[0] * (sum(costs)+1) for _ in range(N+1)]


for i in range(N+1):
    byte = memory[i]
    cost = costs[i]
    for j in range(sum(costs)+1):
        if j < cost: # 현재 앱을 활성화할 만큼 충분한 cost가 없을 경우
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])

        if dp[i][j] >= M:
            answer = min(answer, j)


print(answer)