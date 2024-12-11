# 모래 흩날리기 시작할 때 sand = 0으로 두고 흩날려진 만큼 더한 값을 원래 값에서 빼기
# 그만큼을 알파에 넘기기

# 격자 밖으로 나간 모래의 양
answer = 0
# 왼쪽, 아래쪽, 오른쪽, 위쪽
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

sand_per = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]

# 모래가 왼쪽으로 이동할 때 날리는 비율
s_l_dr = [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0] # 2%, 10%, 7%, 1%, 5%, 10%, 7%, 1%, 2%, 알파
s_l_dc = [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]

# 모래가 위쪽으로 이동할 때 날리는 비율
s_u_dr = [0, -1, 0, 1, -2, -1, 0, 1, 0, -1] # 2%, 10%, 7%, 1%, 5%, 10%, 7%, 1%, 2%, 알파
s_u_dc = [2, 1, 1, 1, 0, -1, -1, -1, -2, 0]

# 모래가 오른쪽으로 이동할 때 날리는 비율
s_r_dr = [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0] # 2%, 10%, 7%, 1%, 5%, 10%, 7%, 1%, 2%, 알파
s_r_dc = [0, 1, 0, -1, 2, 1, 0, -1, 0, 1]

# 모래가 아래쪽으로 이동할 때 날리는 비율
s_d_dr = [0, 1, 0, -1, 2, 1, 0, -1, 0, 1] # 2%, 10%, 7%, 1%, 5%, 10%, 7%, 1%, 2%, 알파
s_d_dc = [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0]

# 모래 흩날리기
def sand(r, c, dir):
    global answer
    sand_move = 0
    sand_fly = 0
    if dir == 0: # 왼쪽으로 이동하는 경우
        for k in range(9):
            nr = r + s_l_dr[k]
            nc = c + s_l_dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                sand_move += int(board[r][c] * sand_per[k])
                board[nr][nc] += int(board[r][c] * sand_per[k])
            else:
                sand_fly += int(board[r][c] * sand_per[k])

    elif dir == 1: # 아래쪽으로 이동하는 경우
        for k in range(9):
            nr = r + s_d_dr[k]
            nc = c + s_d_dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                sand_move += int(board[r][c] * sand_per[k])
                board[nr][nc] += int(board[r][c] * sand_per[k])
            else:
                sand_fly += int(board[r][c] * sand_per[k])

    elif dir == 2: # 오른쪽으로 이동하는 경우
        for k in range(9):
            nr = r + s_r_dr[k]
            nc = c + s_r_dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                sand_move += int(board[r][c] * sand_per[k])
                board[nr][nc] += int(board[r][c] * sand_per[k])
            else:
                sand_fly += int(board[r][c] * sand_per[k])

    elif dir == 3: # 위쪽으로 이동하는 경우
        for k in range(9):
            nr = r + s_u_dr[k]
            nc = c + s_u_dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                sand_move += int(board[r][c] * sand_per[k])
                board[nr][nc] += int(board[r][c] * sand_per[k])
            else:
                sand_fly += int(board[r][c] * sand_per[k])
    # 나머지 값 알파에 넣기
    alpha = board[r][c] - (sand_move + sand_fly)
    if dir == 0:
        nr = r + s_l_dr[-1]
        nc = c + s_l_dc[-1]
    elif dir == 1:
        nr = r + s_d_dr[-1]
        nc = c + s_d_dc[-1]
    elif dir == 2:
        nr = r + s_r_dr[-1]
        nc = c + s_r_dc[-1]
    elif dir == 3:
        nr = r + s_u_dr[-1]
        nc = c + s_u_dc[-1]

    if 0 <= nr < N and 0 <= nc < N:
        board[nr][nc] += alpha
    else:
        sand_fly += alpha
    answer += sand_fly


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
r, c = N//2, N//2
# 한칸씩 이동하기

# 왼쪽, 아래쪽, 오른쪽, 위쪽
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

distance = 0 # 이동할 거리

dir = 0 # 방향

find = False
visited[r][c] = 1
while not find:
    if dir % 2 == 0:
        distance += 1
    move = 0
    while move < distance:
        r += dr[dir]
        c += dc[dir]
        if 0 <= r < N and 0 <= c < N:
            # 모래흩날리기
            sand(r, c, dir)
            if r == 0 and c == 0:
                find = True
                break
            move += 1
    dir += 1
    dir %= 4
print(answer)