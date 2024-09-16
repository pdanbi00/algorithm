# 일단 판을 만들어놓고
# 이동하면서 .으로 채우기
# 위쪽 행, 아래쪽 행, 왼쪽 열, 오른쪽 열에서 .이 제일 먼저 나오는 구간 잘라내기

N = int(input())
board = [['#'] * 101 for _ in range(101)]

dr = [-1, 0, 1, 0] # 북, 동, 남, 서
dc = [0, 1, 0, -1] # 북, 동, 남, 서

dir = 2

r = 50
c = 50

min_r = 50
max_r = 50
min_c = 50
max_c = 50

board[r][c] = '.'

road = list(input())
for move in road:
    if move == 'F':
        r = r + dr[dir]
        c = c + dc[dir]
        board[r][c] = '.'
        max_c, min_c, max_r, min_r = max(max_c, c), min(min_c, c), max(max_r, r), min(min_r, r)

    elif move == 'R':
        dir = (dir + 1) % 4
    elif move == 'L':
        dir = (dir + 3) % 4

for i in range(min_r, max_r+1):
    print(''.join(board[i][min_c:max_c+1]))
