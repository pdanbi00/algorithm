N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= arr[i-1][0]:
            # i-1번째까지의 물건들을 고려한 값이랑 현재 물건의 가치 + 이전 물건들의 가치 중 큰 값
            dp[i][j] = max(arr[i-1][1] + dp[i-1][j-arr[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])