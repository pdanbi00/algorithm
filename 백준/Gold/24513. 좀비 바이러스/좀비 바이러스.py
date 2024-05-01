# bfs로 감염 다 시키고
# 전체 배열 돌면서 개수 세기
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
board = []
visited = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()

ans = [0, 0, 0]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            q.append((i, j, 1, 0))
        elif line[j] == 2:
            q.append((i, j, 2, 0))
            visited[i][j] = 0
    board.append(line)

while q:
    r, c, num, time = q.popleft()
    if board[r][c] != 3:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != -1:
                if board[nr][nc] == 0:
                    q.append((nr, nc, num, time + 1))
                    visited[nr][nc] = time + 1
                    board[nr][nc] = num
                elif board[nr][nc] != -1 and board[nr][nc] != num:
                    if visited[nr][nc] == time + 1:
                        board[nr][nc] = 3
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            ans[0] += 1
        elif board[i][j] == 2:
            ans[1] += 1
        elif board[i][j] == 3:
            ans[2] += 1
print(*ans)