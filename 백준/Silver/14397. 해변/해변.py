N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 홀수행인지 짝수행인지에 따라 다름
drodd = [-1, -1, 0, 0, 1, 1]
dcodd = [0, 1, -1, 1, 0, 1]

dreven = [-1, -1, 0, 0, 1, 1]
dceven = [-1, 0, -1, 1, -1, 0]


answer = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == '#':
            if i % 2 == 1:
                for k in range(len(drodd)):
                    nr = i + drodd[k]
                    nc = j + dcodd[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if board[nr][nc] == '.':
                            answer += 1
            else:
                for k in range(len(dreven)):
                    nr = i + dreven[k]
                    nc = j + dceven[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if board[nr][nc] == '.':
                            answer += 1

print(answer)