def solution(land):
    answer = 0
    N = len(land)
    dp = [[0] * 4 for _ in range(N)]
    for i in range(4):
        dp[0][i] = land[0][i]
        
    for i in range(1, N):
        for j in range(4):
            dp[i][j] = max(dp[i-1][(j+1)%4], dp[i-1][(j+2)%4], dp[i-1][(j+3)%4]) + land[i][j]

    return max(dp[N-1])