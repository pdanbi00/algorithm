N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*(M+2)] + [[0] + row + [0] for row in board] + [[0] * (M+2)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
ans += (N*M) * 2

for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(4):
            nx, ny = i + dr[k], j + dc[k]
            if board[i][j] - board[nx][ny] >= 0:
                ans += board[i][j] - board[nx][ny]
print(ans)
