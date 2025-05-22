N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

X = min(N, M)
ans = 1

for k in range(2, X+1):
    for i in range(N-k+1):
        for j in range(M-k+1):
            if int(board[i][j]) == int(board[i+k-1][j]) and int(board[i+k-1][j]) == int(board[i][j+k-1]) and int(board[i][j+k-1]) == int(board[i+k-1][j+k-1]):
                ans = max(ans, k*k)

print(ans)