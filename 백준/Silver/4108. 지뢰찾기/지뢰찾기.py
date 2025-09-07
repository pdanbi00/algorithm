dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break

    board = [list(input()) for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 0
                for k in range(8):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0 <= nr < R and 0 <= nc < C:
                        if board[nr][nc] == '*':
                            board[i][j] += 1
    for i in range(R):
        for j in range(C):
            print(board[i][j], end = "")
        print()
