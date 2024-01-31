from collections import deque
M, N = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
checked = [[False] * M for _ in range(N)]
q = deque()
next_q = deque()
q.append((0,0))
checked[0][0] = True
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while q:
    now_r, now_c = q.popleft()
    if now_r == N-1 and now_c == M-1:
        print(board[now_r][now_c])
        break
    for k in range(4):
        nr = now_r + dr[k]
        nc = now_c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if checked[nr][nc] == False:
                if board[nr][nc] == 0:
                    q.append((nr, nc))
                    board[nr][nc] = board[now_r][now_c]
                    checked[nr][nc] = True
                elif board[nr][nc] == 1:
                    next_q.append((nr, nc))
                    board[nr][nc] = board[now_r][now_c] + 1
                    checked[nr][nc] = True
    if not q:
        q = next_q
        next_q = deque()