import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
board = [list(input()) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

answer = 0

dr = [-1, -1, 0, 0, 1, 1]
dc = [0, 1, -1, 1, -1, 0]

def dfs(r, c, color):
    global answer
    answer = max(1, answer)
    visited[r][c] = color
    for k in range(6):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == 'X':
                if visited[nr][nc] == -1:
                    answer = max(2, answer)
                    dfs(nr, nc, 1-color)
                elif visited[nr][nc] == color:
                    answer = max(3, answer)

for i in range(N):
    for j in range(N):
        if board[i][j] == 'X' and visited[i][j] == -1:
            dfs(i, j, 0)
print(answer)