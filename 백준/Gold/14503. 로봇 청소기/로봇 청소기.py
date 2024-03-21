N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0
while True:
    # 현재 칸이 청소되어 있지 않으면 청소한다.
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1

    # 현재 칸 주변 4칸이 다 청소된 상태면
    if board[r-1][c] != 0 and board[r][c+1] != 0 and board[r+1][c] != 0 and board[r][c-1] != 0:
        if board[r-dr[d]][c-dc[d]] == 1:
            break
        else:
            r = r - dr[d]
            c = c - dc[d]
    else:
        d = (d+3) % 4
        if board[r + dr[d]][c + dc[d]] == 0:
            r += dr[d]
            c += dc[d]
print(cnt)