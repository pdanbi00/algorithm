N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if i+3 < N: # 1
            temp = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
            if temp > ans:
                ans = temp
        if j+3 < M: # 2
            temp = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
            if temp > ans:
                ans = temp
        if i+1 < N and j+1 < M: # 3
            temp = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
            if temp > ans:
                ans = temp
        if i+2 < N and j+1 < M: # 4
            temp = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1]
            if temp > ans:
                ans = temp
        if i-2 >= 0 and j+1 < M: # 5
            temp = board[i][j] + board[i][j+1] + board[i-1][j+1] + board[i-2][j+1]
            if temp > ans:
                ans = temp
        if i+1 < N and j+2 < M: # 6
            temp = board[i][j] + board[i+1][j] + board[i][j+1] + board[i][j+2]
            if temp > ans:
                ans = temp
        if i+1 < N and j+2 < M: # 7
            temp = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2]
            if temp > ans:
                ans = temp
        if i+2 < N and j+1 < M: # 8
            temp = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
            if temp > ans:
                ans = temp
        if i+2 < N and j+1 < M: # 9
            temp = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+2][j]
            if temp > ans:
                ans = temp
        if i+1 < N and j-2 >= 0: # 10
            temp = board[i][j] + board[i+1][j] + board[i+1][j-1] + board[i+1][j-2]
            if temp > ans:
                ans = temp
        if i+1 < N and j+2 < M: # 11
            temp = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
            if temp > ans:
                ans = temp
        if i+2 < N and j+1 < M: # 12
            temp = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
            if temp > ans:
                ans = temp
        if i+2 < N and j-1 >= 0: # 13
            temp = board[i][j] + board[i+1][j] + board[i+1][j-1] + board[i+2][j-1]
            if temp > ans:
                ans = temp
        if i-1 >= 0 and j+2 < M: # 14
            temp = board[i][j] + board[i][j+1] + board[i-1][j+1] + board[i-1][j+2]
            if temp > ans:
                ans = temp
        if i+1 < N and j+2 < M: # 15
            temp = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
            if temp > ans:
                ans = temp
        if i+1 < N and j+2 < M: # 16
            temp = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]
            if temp > ans:
                ans = temp
        if i-1 >= 0 and j+2 < M: # 17
            temp = board[i][j] + board[i][j+1] + board[i][j+2] + board[i-1][j+1]
            if temp > ans:
                ans = temp
        if i+2 < N and j-1 >= 0: # 18
            temp = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+1][j-1]
            if temp > ans:
                ans = temp
        if i+2 < N and j+1 < M: #19
            temp = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]
            if temp > ans:
                ans = temp
print(ans)