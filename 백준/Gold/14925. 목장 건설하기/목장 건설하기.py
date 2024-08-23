M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]

# DP입니다.....
# dp[i][j] : board[i][j]까지의 제일 긴 정사각형
dp = [[0] * N for _ in range(M)]

for i in range(N):
    if board[0][i] == 0:
        dp[0][i] = 1

for i in range(M):
    if board[i][0] == 0:
        dp[i][0] = 1

for i in range(1, M):
    for j in range(1, N):
        if board[i][j] == 0:
            if dp[i-1][j] != 0 and dp[i][j-1] != 0 and dp[i-1][j-1] != 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = 1
        else:
            dp[i][j] = 0
ans = 0
for i in range(M):
    ans = max(ans, max(dp[i]))
print(ans)