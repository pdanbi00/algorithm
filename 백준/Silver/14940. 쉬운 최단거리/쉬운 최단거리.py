# bfs다 분명하다
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
check = [[-1] * m for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            q.append((i, j))
            check[i][j] = 0
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < n and 0 <= nc < m:
                        if board[nr][nc] == 1 and check[nr][nc] == -1:
                            q.append((nr, nc))
                            check[nr][nc] = check[r][c] + 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            check[i][j] = 0
for i in range(n):
    print(*check[i])