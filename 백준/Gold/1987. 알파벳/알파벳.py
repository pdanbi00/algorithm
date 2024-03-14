import sys
input = sys.stdin.readline
R, C = map(int, input().split())
board = [input() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 1
def dfs(r, c, alpha):
    global ans
    visited[r][c] = 1
    alpha += board[r][c]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if visited[nr][nc] == 0 and board[nr][nc] not in alpha:
                dfs(nr, nc, alpha)
                visited[nr][nc] = 0
    if len(alpha) > ans:
        ans = len(alpha)

dfs(0, 0, '')
print(ans)