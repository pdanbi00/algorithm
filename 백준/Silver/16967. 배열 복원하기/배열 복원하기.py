H, W, X, Y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H+X)]

arr = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i >= X and j >= Y:
            arr[i][j] = board[i][j] - arr[i-X][j-Y]
        else:
            arr[i][j] = board[i][j]
for i in range(H):
    print(*arr[i])