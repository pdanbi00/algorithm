from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

cnt = 0
visited = [[False] * N for _ in range(M)]

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        r, c = q.popleft()
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < M and 0 <= nc < N:
                if not visited[nr][nc] and board[nr][nc] == 1:
                    q.append((nr, nc))
                    visited[nr][nc] = True

for i in range(M):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)