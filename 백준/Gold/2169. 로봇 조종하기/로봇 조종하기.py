# DP
# 왼쪽, 오른쪽, 아래쪽으로만 이동 가능
# -> 위에서 오는 경우, 왼쪽에서 오는 경우 / 위쪽에서 오는 경우, 오른쪽에서 오는 경우 비교해서 가장 큰 값으로 갱신

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = board[0][0]
for i in range(1, M):
    dp[0][i] = board[0][i]
    dp[0][i] += dp[0][i-1]

for i in range(1, N):
    tmp1 = [0] * M # 왼쪽에서 오른쪽으로 가는 최대값
    tmp2 = [0] * M # 오른쪽에서 왼쪽으로 가는 최대값

    for j in range(M):
        # 첫번째 칸은 무조건 위에서 오는 경우 밖에 없음
        if j == 0:
            tmp1[j] = board[i][j] + dp[i-1][j]
            tmp2[M-1-j] = board[i][M-1-j] + dp[i-1][M-1-j]
        else:
            tmp1[j] = board[i][j] + max(dp[i-1][j], tmp1[j-1])
            tmp2[M-1-j] = board[i][M-1-j] + max(dp[i-1][M-1-j], tmp2[M-j])
    for j in range(M):
        dp[i][j] = max(tmp1[j], tmp2[j])

print(dp[N-1][M-1])