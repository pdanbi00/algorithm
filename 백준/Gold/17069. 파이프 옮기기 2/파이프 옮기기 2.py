N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1 # dp[i][j][d] i행 j열에 d방향으로 올 수 있는 경우의 수

for i in range(N):
    for j in range(N):
        # 가로일 경우
        if j+1 < N and i+1 < N:
            if board[i][j+1] == 0 and board[i+1][j] == 0 and board[i+1][j+1] == 0:
                dp[i+1][j+1][2] += dp[i][j][0]
        if j+1 < N and board[i][j+1] == 0:
            dp[i][j+1][0] += dp[i][j][0]
        # 세로일 경우
        if j + 1 < N and i + 1 < N:
            if board[i][j + 1] == 0 and board[i + 1][j] == 0 and board[i + 1][j + 1] == 0:
                dp[i + 1][j + 1][2] += dp[i][j][1]
        if i + 1 < N and board[i + 1][j] == 0:
            dp[i + 1][j][1] += dp[i][j][1]
        # 대각선일 경우
        if j + 1 < N and i + 1 < N:
            if board[i][j + 1] == 0 and board[i + 1][j] == 0 and board[i + 1][j + 1] == 0:
                dp[i + 1][j + 1][2] += dp[i][j][2]
        if j + 1 < N and board[i][j + 1] == 0:
            dp[i][j + 1][0] += dp[i][j][2]
        if i + 1 < N and board[i + 1][j] == 0:
            dp[i + 1][j][1] += dp[i][j][2]

print(dp[i][j][0] + dp[i][j][1] + dp[i][j][2])