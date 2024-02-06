N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0

def solution(x, y, N):
    global white, blue
    color = board[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if board[i][j] != color:
                solution(x, y, N//2)
                solution(x+N//2, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 1:
        blue += 1
    else:
        white += 1
solution(0, 0, N)
print(white)
print(blue)