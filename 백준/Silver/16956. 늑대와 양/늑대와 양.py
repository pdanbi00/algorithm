R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if board[i][j] == 'W':
            for k in range(4):
                ni, nj = i + dr[k], j + dc[k]
                if 0 <= ni < R and 0 <= nj < C:
                    if board[ni][nj] == 'S':
                        print(0)
                        exit()

print(1)
for i in range(R):
    for j in range(C):
        if board[i][j] == '.':
            print('D', end="")
        else:
            print(board[i][j], end="")
    print()