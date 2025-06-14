from collections import deque
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
PR, PC = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

P = [1, 0, 3, 2]
Q = [3, 2, 1, 0]
dirs = ['U', 'R', 'D', 'L']

def func(i, j, d):
    cnt = 0
    r, c, di = i, j, d
    while True:
        cnt += 1
        r += dr[di]
        c += dc[di]
        if 0 <= r < N and 0 <= c < M:
            if r == i and c == j and di == d:
                return 1e9
            if board[r][c] == '.':
                continue
            elif board[r][c] == 'C':
                return cnt
            elif board[r][c] == '/':
                di = P[di]
            elif board[r][c] == '\\':
                di = Q[di]
        else:
            break
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
print(dirs[idx])
if tmp == 1e9:
    print("Voyager")
else:
    print(tmp)