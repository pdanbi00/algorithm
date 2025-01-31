from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, s_r, s_c, f_r, f_c = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 벽 위치 저장
walls = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            walls.append((i, j))

def move(r, c):
    q = deque()
    q.append((r, c))
    board[s_r][s_c] = 2

    while q:
        now_r, now_c = q.popleft()

        if now_r == f_r and now_c == f_c:
            return board[now_r][now_c] - 2

        for k in range(4):
            nr = now_r + dr[k]
            nc = now_c + dc[k]

            if nr < 0 or nc < 0 or nr > (N - H) or nc > (M - W) or board[nr][nc] or not check(nr, nc):
                continue
            board[nr][nc] = board[now_r][now_c] + 1
            q.append((nr, nc))

    return -1

def check(start_r, start_c):
    min_r, max_r = start_r, start_r + H
    min_c, max_c = start_c, start_c + W

    for (r, c) in walls:
        if min_r <= r < max_r and min_c <= c < max_c:
            return False
    return True

s_r, s_c, f_r, f_c = s_r - 1, s_c - 1, f_r - 1, f_c - 1
print(move(s_r, s_c))