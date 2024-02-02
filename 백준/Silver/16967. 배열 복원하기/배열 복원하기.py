H, W, X, Y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H+X)]

for i in range(H):
    for j in range(W):
        board[i+X][j+Y] -= board[i][j]
for i in range(H):
    print(*board[i][:W])