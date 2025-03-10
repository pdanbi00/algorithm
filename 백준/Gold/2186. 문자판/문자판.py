import sys
input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(N)]
target = list(input().rstrip())
l = len(target)

dp = [[[-1] * l for _ in range(M)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = 0

def dfs(r, c, idx):
    if idx == len(target):
        return 1

    if dp[r][c][idx] != -1:
        return dp[r][c][idx]

    dp[r][c][idx] = 0

    for k in range(4):
        nr, nc = r, c
        for p in range(K):
            nr += dr[k]
            nc += dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == target[idx]:
                    dp[r][c][idx] += dfs(nr, nc, idx + 1)
            else:
                break
    return dp[r][c][idx]

for i in range(N):
    for j in range(M):
        if board[i][j] == target[0]:
            answer += dfs(i, j, 1)

print(answer)