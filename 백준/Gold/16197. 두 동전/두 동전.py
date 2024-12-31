# BFS
from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
coins = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    while q:
        r1, c1, r2, c2, cnt = q.popleft()
        if cnt >= 10:
            return -1
        for k in range(4):
            nr1 = r1 + dr[k]
            nc1 = c1 + dc[k]
            nr2 = r2 + dr[k]
            nc2 = c2 + dc[k]
            if 0 <= nr1 < N and 0 <= nc1 < M and 0 <= nr2 < N and 0 <= nc2 < M:
                if board[nr1][nc1] == '#':
                    nr1, nc1 = r1, c1
                if board[nr2][nc2] == '#':
                    nr2, nc2 = r2, c2
                q.append((nr1, nc1, nr2, nc2, cnt+1))
            elif not (0 <= nr1 < N and 0 <= nc1 < M) and not (0 <= nr2 < N and 0 <= nc2 < M):
                continue
            else: # 하나만 범위 안에 있는 경우
                return cnt + 1
    return -1

for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append(i)
            coins.append(j)
q = deque()
q.append([*coins, 0])

print(bfs())