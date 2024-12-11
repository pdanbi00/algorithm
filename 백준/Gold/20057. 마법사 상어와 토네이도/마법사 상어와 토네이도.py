N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0 # 밖으로 나간 모래 양

# 왼쪽, 아래쪽, 오른쪽, 위쪽
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

r, c = N // 2, N // 2

# 왼쪽 방향으로 퍼질때
left = [(-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02), (0, -1, 0)]
# 아래쪽 방향으로 퍼질때
down = [(-y, x, z) for x, y, z in left]
# 오른쪽 방향으로 퍼질때
right = [(x, -y, z) for x, y, z in left]
# 위쪽 방향으로 퍼질때
up = [(y, -x, z) for x, y, z in left]

directions = {0 : left, 1 : down, 2 : right, 3 : up}

# 모래 흩날리기
def sand(r, c, direction):
    global answer
    total = 0 # 알파를 구하기 위한

    for dr, dc, z in direction:
        nr = r + dr
        nc = c + dc
        if z == 0: # 알파인 경우
            new_sand = board[r][c] - total
        else:
            new_sand = int(board[r][c] * z)
            total += new_sand
        if 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] += new_sand
        else:
            answer += new_sand

distance = 0 # 이동할 거리
dir = 0 # 방향
find = False

while not find:
    if dir % 2 == 0:
        distance += 1
    move = 0
    for _ in range(distance):
        r += dr[dir]
        c += dc[dir]
        if 0 <= r < N and 0 <= c < N:
            # 모래흩날리기
            sand(r, c, directions[dir])
            if r == 0 and c == 0:
                find = True
                break
            move += 1
    dir += 1
    dir %= 4
print(answer)