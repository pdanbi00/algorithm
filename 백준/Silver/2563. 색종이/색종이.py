N = int(input())
board = [[0] * 100 for _ in range(100)]

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            board[b+i][a+j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            ans += 1

print(ans)