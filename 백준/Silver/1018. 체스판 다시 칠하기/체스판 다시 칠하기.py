N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ans = 64
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0 and board[i+k][j+l] != 'B':
                        cnt += 1
                    elif l % 2 == 1 and board[i+k][j+l] != 'W':
                        cnt += 1
                else:
                    if l % 2 == 0 and board[i+k][j+l] != 'W':
                        cnt += 1
                    elif l % 2 == 1 and board[i+k][j+l] != 'B':
                        cnt += 1
        ans = min(ans, cnt)
        cnt = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0 and board[i+k][j+l] != 'W':
                        cnt += 1
                    elif l % 2 == 1 and board[i+k][j+l] != 'B':
                        cnt += 1
                else:
                    if l % 2 == 0 and board[i+k][j+l] != 'B':
                        cnt += 1
                    elif l % 2 == 1 and board[i+k][j+l] != 'W':
                        cnt += 1

        ans = min(ans, cnt)

print(ans)

