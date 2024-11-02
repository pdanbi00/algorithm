from collections import deque
import sys
input = sys.stdin.readline
R, C, N = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]
if N == 1:
    for i in range(R):
        for j in range(C):
            if board[i][j] != '.':
                board[i][j] = 'O'
            print(board[i][j], end='')
        print()
else:
    time = 2
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                board[i][j] = 1
            else:
                board[i][j] = 3

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while time < N:
        time += 1
        visited = [[0] * C for _ in range(R)]
        q = deque()
        for i in range(R):
            for j in range(C):
                if board[i][j] == 1:
                    q.append((i, j))
                elif board[i][j] == '.':
                    board[i][j] = 3
                elif board[i][j] == 3:
                    board[i][j] = 2
                elif board[i][j] == 2:
                    board[i][j] = 1
        while q:
            r, c = q.popleft()
            board[r][c] = '.'
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < R and 0 <= nc < C:
                    board[nr][nc] = '.'

    for i in range(R):
        for j in range(C):
            if board[i][j] != '.':
                board[i][j] = 'O'
            print(board[i][j], end='')
        print()

'''
6 7 1
.......
...O...
....O..
.......
OO.....
OO.....
'''