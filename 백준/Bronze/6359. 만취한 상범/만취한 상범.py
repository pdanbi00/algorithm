T = int(input())
board = [[0] * 101 for _ in range(101)]
for i in range(1, 101):
    for j in range(1, 101):
        if j % i == 0:
            board[i][j] = 1

for _ in range(T):
    N = int(input())
    arr = [0] * 101
    ans = 0
    for i in range(1, N+1):
        tmp = 0
        for j in range(1, N+1):
            if board[j][i] == 1:
                tmp += 1
        if tmp % 2 == 1:
            ans += 1
    print(ans)