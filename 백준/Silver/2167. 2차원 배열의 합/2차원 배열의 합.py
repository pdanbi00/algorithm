import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

sum_board = [[0] * M for _ in range(N)]
pre = 0
for i in range(N):
    for j in range(M):
        sum_board[i][j] = pre + board[i][j]
        pre = sum_board[i][j]

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    tmp = sum_board[x2][y2]
    # 왼쪽 빼기
    for i in range(x1, x2+1):
        for j in range(y1):
            tmp -= board[i][j]
    for i in range(x1, x2):
        if y2 + 1 < M:
            for j in range(y2 + 1, M):
                tmp -= board[i][j]

    # 아래쪽 빼기
    if x1 - 1 >= 0:
        tmp -= sum_board[x1-1][M-1]

    print(tmp)