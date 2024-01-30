from collections import deque

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]
T = int(input())
for _ in range(T):
    I = int(input())
    now_r, now_c = map(int, input().split())
    to_r, to_c = map(int, input().split())

    q = deque()
    board = [[0] * I for _ in range(I)]
    board[now_r][now_c] = 1
    q.append((now_r, now_c))
    while q:
        r, c = q.popleft()
        if r == to_r and c == to_c:
            print(board[r][c]-1) # 1부터 시작하니깐 -1 해줘야 됨.
            break
        for k in range(8):
            nr = r+dr[k]
            nc = c+dc[k]
            if 0 <= nr < I and 0 <= nc < I:
                if board[nr][nc] == 0:
                    q.append((nr, nc))
                    board[nr][nc] = board[r][c] + 1
