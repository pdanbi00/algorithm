N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * N for _ in range(N)] for _ in range(3)]
# 0 : 가로, 1 : 세로, 2 : 대각선

dp[0][0][1] = 1

# 가로 값들 초기화
for i in range(2, N):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]
        
for i in range(1, N):
    for j in range(1, N):
        # 대각선 놓기
        if board[i][j] == 0 and board[i][j-1] == 0 and board[i-1][j] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
            
        if board[i][j] == 0:
            # 가로 놓기
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            
            # 세로 놓기
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])