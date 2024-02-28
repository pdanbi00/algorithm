N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 and j > 0:
            dp[i][j] = dp[i][j-1] + board[i][j]
        elif i > 0 and j == 0:
            dp[i][j] = dp[i-1][j] + board[i][j]
        else:
            dp[i][j] = board[i][j]
if N >= 2 and M >= 2:
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + board[i][j]

print(dp[N-1][M-1])