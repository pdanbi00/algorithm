garo = 0
sero = 0
N = int(input())
board = [list(input()) for _ in range(N)]
for i in range(N):
    j = 0
    while j < N-1:
        if board[i][j] == '.' and board[i][j+1] == '.':
            garo += 1
            while j < N:
                if board[i][j] == 'X':
                    break
                j += 1
        j += 1

for j in range(N):
    i = 0
    while i < N-1:
        if board[i][j] == '.' and board[i+1][j] == '.':
            sero += 1
            while i < N:
                if board[i][j] == 'X':
                    break
                i += 1
        i += 1

print(garo, sero)