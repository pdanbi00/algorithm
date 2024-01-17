def check(arr, start_row, end_row, start_col, end_col):
    n = len(arr)
    ans = 1
    for i in range(start_row, end_row+1):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
    for i in range(start_col, end_col+1):
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
    return ans

N = int(input())
board = [list(input()) for _ in range(N)]

max_candy = 0
for i in range(N):
    for j in range(N):
        if i + 1 < N: # 아래랑 바꾸기
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            tmp = check(board, i, i+1, j, j)
            if tmp > max_candy:
                max_candy = tmp
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        if j + 1 < N: # 오른쪽이랑 바꾸기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            tmp = check(board, i, i, j, j+1)
            if tmp > max_candy:
                max_candy = tmp
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
print(max_candy)