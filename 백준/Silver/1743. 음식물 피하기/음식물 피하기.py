from collections import deque
N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

ans = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 1 and visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    cnt += 1
    return cnt

visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and visited[i][j] == 0:
            ans = max(ans, bfs(i, j))

print(ans)