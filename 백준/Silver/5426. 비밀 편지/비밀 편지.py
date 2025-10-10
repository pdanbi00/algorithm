from math import sqrt

T = int(input())
for _ in range(T):
    line = list(input())
    N = int(sqrt(len(line)))
    board = [[0] * N for _ in range(N)]

    idx = 0
    for i in range(N):
        for j in range(N):
            board[N-1-j][i] = line[idx]
            idx += 1

    answer = ''
    for i in range(N):
        for j in range(N):
            answer += board[i][j]
    print(answer)