from math import sqrt
line = input()
N = len(line)

R, C = 0, 0
for i in range(int(sqrt(N)), 0, -1):
    if N % i == 0:
        R = i
        C = N // i
        break

board = [[''] * C for _ in range(R)]

idx = 0
for j in range(C):
    for i in range(R):
        board[i][j] = line[idx]
        idx += 1

answer = ''
for i in range(R):
    for j in range(C):
        answer += board[i][j]

print(answer)