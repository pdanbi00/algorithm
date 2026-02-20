from collections import deque

N = int(input())
board = [list(input().split()) for _ in range(N)]

dr = [0, 1]
dc = [1, 0]

max_v = -1e9
min_v = 1e9

q = deque() # r, c, total
q.append((0, 0, int(board[0][0])))

while q:
    r, c, total = q.popleft()

    if r == N-1 and c == N-1:
        max_v = max(max_v, total)
        min_v = min(min_v, total)
        continue

    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            for p in range(2):
                nnr = nr + dr[p]
                nnc = nc + dc[p]
                if 0 <= nnr < N and 0 <= nnc < N:
                    if board[nr][nc] == '+':
                        tmp = total + int(board[nnr][nnc])
                        q.append((nnr, nnc, tmp))
                    elif board[nr][nc] == '-':
                        tmp = total - int(board[nnr][nnc])
                        q.append((nnr, nnc, tmp))
                    elif board[nr][nc] == '*':
                        tmp = total * int(board[nnr][nnc])
                        q.append((nnr, nnc, tmp))


print(max_v, min_v)