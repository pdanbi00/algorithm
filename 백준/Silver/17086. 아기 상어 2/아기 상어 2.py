from collections import deque

N, M = map(int, input().split())
board = []
shark = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j] == 1:
            shark.append((i, j))
    board.append(arr)

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[-1] * M for _ in range(N)]
    visited[x][y] = 0
    while q:
        r, c = q.popleft()

        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == -1 and board[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                elif visited[nr][nc] == -1 and board[nr][nc] == 1:
                    return visited[r][c] + 1
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            ans = max(ans, bfs(i, j))
print(ans)