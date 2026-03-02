# DP...
from collections import deque

N, M = map(int, input().split())
board = []
for i in range(N):
    arr = list(input())
    for j in range(M):
        if arr[j] == 'R':
            r_r, r_c = i, j
    board.append(arr)

dr = [-1, 0, 1]
dc = [-1, -1, -1]

dp = [[-1] * M for _ in range(N)]
dp[r_r][r_c] = 0

answer = 0

possible = False
for c in range(r_c, M):
    for r in range(N):
        if board[r][c] == '#':
            continue

        for k in range(3):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if dp[nr][nc] != -1:
                    if board[r][c] == 'C':
                        dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)
                    elif board[r][c] == '.':
                        dp[r][c] = max(dp[r][c], dp[nr][nc])
                    elif board[r][c] == 'O':
                        possible = True
                        dp[r][c] = max(dp[r][c], dp[nr][nc])
                        answer = max(answer, dp[r][c])



if possible:
    print(answer)
else:
    print(-1)