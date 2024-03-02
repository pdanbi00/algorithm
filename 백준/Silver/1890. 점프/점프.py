# DP라니...
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            print(dp[N-1][N-1])
            break
        cur = board[i][j]
        if j + cur < N: # 오른쪽으로 이동
            dp[i][j+cur] += dp[i][j]
        if i + cur < N: # 아래쪽으로 이동
            dp[i+cur][j] += dp[i][j]
