def compression(r, c, N):
    global answer
    num = board[r][c]
    for i in range(r, r+N):
        for j in range(c, c+N):
            if board[i][j] != num:
                answer += "("
                compression(r, c, N//2)
                compression(r, c + N//2, N//2)
                compression(r + N // 2, c, N // 2)
                compression(r + N // 2, c + N // 2, N // 2)
                answer += ")"
                return
    answer += num

N = int(input())
board = [list(input()) for _ in range(N)]
answer = ""
compression(0, 0, N)
print(answer)