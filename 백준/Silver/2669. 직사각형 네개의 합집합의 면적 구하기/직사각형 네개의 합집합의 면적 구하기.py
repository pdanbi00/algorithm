board = [[0] * 101 for _ in range(101)]

for _ in range(4):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            board[i][j] += 1

answer = 0
for i in range(101):
    for j in range(101):
        if board[i][j] != 0:
            answer += 1

print(answer)