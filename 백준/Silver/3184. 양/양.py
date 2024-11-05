# 각 영역마다 bfs 돌면서 양 개수, 늑대 개수 세서
# 양 개수보다 늑대 개수가 많으면 + 늑대수
# 양 개수가 늑대 개수보다 많으면 + 양 개수
from collections import deque

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

sheep = 0
wolf = 0

def bfs(i, j):
    global sheep, wolf
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    s = 0 # 이 영역 안에서의 양 마리 수
    w = 0 # 이 영역 안에서의 늑대 마리 수
    if board[i][j] == 'o':
        s += 1
    elif board[i][j] == 'v':
        w += 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if visited[nr][nc] == 0 and board[nr][nc] != '#':
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    if board[nr][nc] == 'o':
                        s += 1
                    elif board[nr][nc] == 'v':
                        w += 1
    if s > w:
        sheep += s
    else:
        wolf += w

for i in range(R):
    for j in range(C):
        if board[i][j] != '#' and visited[i][j] == 0:
            bfs(i, j)
print(sheep, wolf)