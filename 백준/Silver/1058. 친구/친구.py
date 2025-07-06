N = int(input())
board = [list(input()) for _ in range(N)]
ans = [0] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if board[i][j] == 'Y':
                ans[i] += 1
            else:
                for k in range(N):
                    if i != k and j != k:
                        if board[i][k] == 'Y' and board[j][k] == 'Y':
                            ans[i] += 1
                            break

print(max(ans))