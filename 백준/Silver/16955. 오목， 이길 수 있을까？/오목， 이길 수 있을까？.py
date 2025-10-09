board = [list(input()) for _ in range(10)]

possible = False

def check(r, c):
    # 세로 확인
    if r + 4 < 10:
        cnt = 0
        for i in range(5):
            if board[r+i][c] == 'X':
                cnt += 1
            elif board[r+i][c] != '.':
                cnt = 0

        if cnt >= 4:
            return True

    if r - 4 >= 0:
        cnt = 0
        for i in range(5):
            if board[r-i][c] == 'X':
                cnt += 1
            elif board[r-i][c] != '.':
                cnt = 0

        if cnt >= 4:
            return True

    # 가로 확인
    if c + 4 < 10:
        cnt = 0
        for j in range(5):
            if board[r][c + j] == 'X':
                cnt += 1
            elif board[r][c + j] != '.':
                cnt = 0
        if cnt >= 4:
            return True

    if c - 4 >= 0:
        cnt = 0
        for j in range(5):
            if board[r][c - j] == 'X':
                cnt += 1
            elif board[r][c - j] != '.':
                cnt = 0
        if cnt >= 4:
            return True

    # 오른쪽 아래 대각선 확인
    if r + 4 < 10 and c + 4 < 10:
        cnt = 0
        for i in range(5):
            if board[r+i][c+i] == 'X':
                cnt += 1
            elif board[r+i][c+i] != '.':
                cnt = 0
        if cnt >= 4:
            return True

    # 오른쪽 위 대각선 확인
    if r - 4 >= 0 and c + 4 < 10:
        cnt = 0
        for i in range(5):
            if board[r - i][c + i] == 'X':
                cnt += 1
            elif board[r - i][c + i] != '.':
                cnt = 0
        if cnt >= 4:
            return True

    # 왼쪽 아래 대각선 확인
    if r + 4 < 10 and c - 4 >= 0:
        cnt = 0
        for i in range(5):
            if board[r+i][c-i] == 'X':
                cnt += 1
            elif board[r+i][c-i] != '.':
                cnt = 0
        if cnt >= 4:
            return True

    # 왼쪽 위 대각선 확인
    if r - 4 >= 0 and c - 4 >= 0:
        cnt = 0
        for i in range(5):
            if board[r-i][c-i] == 'X':
                cnt += 1
            elif board[r-i][c-i] != '.':
                cnt = 0
        if cnt >= 4:
            return True

    return False

for x in range(10):
    for y in range(10):
        if board[x][y] != 'O':
            result = check(x, y)
            if result:
                possible = True
                break

    if possible:
        break

if possible:
    print(1)
else:
    print(0)


'''
.......X..
......X...
.....X....
....X.....
..........
..........
..........
..........
..OOOO....
..........
'''