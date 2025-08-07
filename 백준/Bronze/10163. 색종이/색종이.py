import sys
input = sys.stdin.readline
N = int(input())
board = [[0] * 1001 for _ in range(1001)]

answer = [0] * (N+1)

for num in range(1, N+1):
    c, r, w, h = map(int, input().split())
    for i in range(h):
        for j in range(w):
            if board[1000-r-i][c+j] != 0:
                answer[board[1000-r-i][c+j]] -= 1
            answer[num] += 1
            board[1000-r-i][c+j] = num

for i in range(1, N+1):
    print(answer[i])