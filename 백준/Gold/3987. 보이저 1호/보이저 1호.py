from collections import deque
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
PR, PC = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def func(i, j, d):
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    cnt = 0
    q = deque()
    q.append((i, j, d))
    visited[i][j][d] = True
    while q:
        cnt += 1
        r, c, d = q.popleft()
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc][d]:
                if board[nr][nc] == '.':
                    q.append((nr, nc, d))
                    visited[nr][nc][d] = True
                elif board[nr][nc] == 'C':
                    return cnt
                elif board[nr][nc] == '/':
                    visited[nr][nc][d] = True
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    elif d == 3:
                        d = 2
                    q.append((nr, nc, d))


                elif board[nr][nc] == '\\':
                    visited[nr][nc][d] = True
                    if d == 0:
                        d = 3
                    elif d == 1:
                        d = 2
                    elif d == 2:
                        d = 1
                    elif d == 3:
                        d = 0
                    q.append((nr, nc, d))

            else:
                return 1e9


    return cnt

answer = []
for k in range(4):
    answer.append(func(PR-1, PC-1, k))

tmp = answer[0]
idx = 0
for i in range(1, 4):
    if answer[i] > tmp:
        tmp = answer[i]
        idx = i
if idx == 0:
    print('U')
elif idx == 1:
    print('R')
elif idx == 2:
    print('D')
else:
    print('L')
if tmp == 1e9:
    print("Voyager")
else:
    print(tmp)