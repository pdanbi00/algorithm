# 이것은 그냥 대충 봐도 DP
# 어느 방향에서 온지 확인해야하니깐
# 3방향 정보까지 담을 수 있도록 3차원으로

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[1e9] * M for _ in range(N)] for _ in range(3)]
# dp[0][i][j] : 직전 방향에서 왼쪽 대각선 방향으로 진행해온 i행 j열까지의 최소값
# dp[1][i][j] : 직전 방향에서 아래쪽 방향으로 진행해온 i행 j열까지의 최소값
# dp[2][i][j] : 직전 방향에서 오른쪽 대각선 방향으로 진행해온 i행 j열까지의 최소값

for i in range(3):
    for j in range(M):
        dp[i][0][j] = board[0][j]

for i in range(1, N):
    for j in range(M):
        # 마지막 열이 아니면 오른쪽 위에서 오는거 가능
        if j < M-1:
            dp[0][i][j] = min(dp[1][i-1][j+1], dp[2][i-1][j+1]) + board[i][j]
        # 첫번째 열이 아니면 왼쪽 위에서 오는거 가능
        if j > 0:
            dp[2][i][j] = min(dp[0][i-1][j-1], dp[1][i-1][j-1]) + board[i][j]
        dp[1][i][j] = min(dp[0][i-1][j], dp[2][i-1][j]) + board[i][j]

print(min(min(dp[0][N-1]), min(dp[1][N-1]), min(dp[2][N-1])))

'''
6 4
5 8 5 1
3 5 8 4
9 77 65 5
2 1 5 2
5 98 1 5
4 95 67 58
'''