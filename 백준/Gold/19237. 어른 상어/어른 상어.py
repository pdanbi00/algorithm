N, M, K = map(int, input().split())
shark_info = {}
board = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] != 0:
            shark_info[arr[j]] = [i, j]
            arr[j] = [arr[j], K]
    board.append(arr)

shark_dir = list(map(int, input().split()))
for i in range(M):
    shark_info[i+1].append(shark_dir[i]-1)

# 주어진 방향은 다 상하좌우
shark_dir_info = {}
for i in range(1, M+1):
    dir_info = [list(map(int, input().split())) for _ in range(4)]
    shark_dir_info[i] = dir_info

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move():
    new_board = [[0] * N for _ in range(N)]
    for shark in shark_info: # 현재 남아있는 상어 번호
        r, c, d = shark_info[shark]
        find = False
        # 상하좌우 아무 냄새가 없는 칸 찾기
        for k in range(4):
            nr = r + dr[shark_dir_info[shark][d][k]-1]
            nc = c + dc[shark_dir_info[shark][d][k]-1]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 0:
                    if new_board[nr][nc] == 0:
                        new_board[nr][nc] = [[shark, shark_dir_info[shark][d][k]-1]]
                    else:
                        new_board[nr][nc].append([shark, shark_dir_info[shark][d][k]-1])
                    find = True
                    break
        # 상하좌우 아무 냄새가 없는 칸이 없다면
        if not find:
            for k in range(4):
                nr = r + dr[shark_dir_info[shark][d][k] - 1]
                nc = c + dc[shark_dir_info[shark][d][k] - 1]
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] != 0 and board[nr][nc][0] == shark:
                        if new_board[nr][nc] == 0:
                            new_board[nr][nc] = [[shark, shark_dir_info[shark][d][k] - 1]]
                        else:
                            new_board[nr][nc].apppend([shark, shark_dir_info[shark][d][k] - 1])
                        break

    # 모든 상어가 이동 한 후 한 칸에 상어가 여러마리 있으면 쫓아내기
    for i in range(N):
        for j in range(N):
            if new_board[i][j] != 0 and len(new_board[i][j]) > 1:
                new_board[i][j].sort()
                for idx in range(1, len(new_board[i][j])):
                    del shark_info[new_board[i][j][idx][0]]
                shark_info[new_board[i][j][0][0]] = [i, j, new_board[i][j][0][1]]
                board[i][j] = [new_board[i][j][0][0], K+1]
            elif new_board[i][j] != 0:
                shark_info[new_board[i][j][0][0]] = [i, j, new_board[i][j][0][1]]
                board[i][j] = [new_board[i][j][0][0], K + 1]

def minus():
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = 0

time = 0

while time <= 1000:
    if len(shark_info) == 1 and 1 in shark_info:
        break
    move()
    minus()
    time += 1

# 이동한 후 한 칸에 여러마리 상어가 남아있으면 가장 작은 번호를 가진 상어 제외하고 모두 쫓겨남
if time > 1000:
    print(-1)
else:
    print(time)