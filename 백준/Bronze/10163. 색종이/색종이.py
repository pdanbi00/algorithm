N = int(input())
board = [[0] * 1001 for _ in range(1001)]

for num in range(1, N+1):
    c, r, w, h = map(int, input().split())
    for i in range(h):
        for j in range(w):
            board[1000-r-i][c+j] = num

answer = [0] * (N+1)
for i in range(1001):
    for j in range(1001):
        for k in range(1, N+1):
            if board[i][j] == k:
                answer[k] += 1
                break

for i in range(1, N+1):
    print(answer[i])