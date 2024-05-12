# M : 세로      N : 가로
from collections import deque


M, N, K = map(int ,input().split())
board = [[0]*N for _ in range(M)]
cnt = 0
ans = []
for p in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    y1 = M - y1
    y2 = M - y2
    for i in range(y2, y1):
        for j in range(x1, x2):
            board[i][j] += 1
visited = [[0]*N for _ in range(M)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and visited[i][j] == 0:
            count = 1
            cnt += 1
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < M and 0 <= nc < N:
                        if visited[nr][nc] == 0 and board[nr][nc] == 0:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
                            count += 1
            ans.append(count)
print(cnt)
ans.sort()
print(*ans)