from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(M)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * N for _ in range(M)]
w_cnt = 0
b_cnt = 0

def bfs(i, j, col):
    global w_cnt, b_cnt
    q = deque()
    visited[i][j] = True
    cnt = 1
    q.append((i, j))
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < M and 0 <= nc < N:
                if board[nr][nc] == col and visited[nr][nc] == False:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    cnt += 1
    if col == 'W':
        w_cnt += cnt * cnt
    else:
        b_cnt += cnt * cnt


for i in range(M):
    for j in range(N):
        if visited[i][j] == False:
            if board[i][j] == 'W':
                bfs(i, j, 'W')
            else:
                bfs(i, j, 'B')

print(w_cnt, b_cnt)