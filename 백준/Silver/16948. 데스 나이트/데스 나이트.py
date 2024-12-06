from collections import deque

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

N = int(input())
board = [[-1] * N for _ in range(N)]

r1, c1, r2, c2 = map(int, input().split())
q = deque()
q.append((r1, c1))
board[r1][c1] = 0

answer = -1

while q:
    r, c = q.popleft()
    if r == r2 and c == c2:
        answer = board[r][c]
        break
    for k in range(6):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == -1:
                q.append((nr, nc))
                board[nr][nc] = board[r][c] + 1
print(answer)