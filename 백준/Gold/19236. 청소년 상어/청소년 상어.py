# 1. 상어가 (0, 0)에 있는 물고기 먹기
#   - 상어 방향은 (0, 0)에 있던 물고기의 방향이 됨

# 2. 물고기 이동하기
#   - 번호가 작은 물고기부터 순서대로 이동
#   - 빈칸 혹은 다른 물고기가 있는 칸으로 이동 가능(상어가 있거나 범위 넘는 칸은 불가능)
#   - 없으면 반시계방향으로 45도씩 회전
#   - 그래도 안되면 이동 안함.
#   - 물고기 이동은 다른 물고기랑 위치 바꾸는 방식으로 진행

# 3. 상어 이동하기
#   - 물고기가 없는 칸으로는 이동 불가능
#   - 물고기가 있는 칸으로 이동하면 그 칸에 있는 물고기 먹고, 그 물고기 방향을 갖게 됨.

# 2, 3번 반복
from collections import deque
from copy import deepcopy

arr = [list(map(int, input().split())) for _ in range(4)]
board = []
for i in range(4):
    a = []
    for j in range(0, 8, 2):
        a.append([arr[i][j], arr[i][j+1]-1])
    board.append(a)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

shark_r = shark_c = shark_d = 0
shark_d = board[0][0][1]
eaten = board[0][0][0]

board[0][0] = -1 # 상어 위치 표현

answer = eaten

# 물고기 이동
def fish_move(fishes):
    alive = []
    fish_info = {} # 각 물고기번호의 위치(행, 열)
    # 살아있는 물고기 번호 확인
    for i in range(4):
        for j in range(4):
            if fishes[i][j] != -1 and fishes[i][j] != 0:
                alive.append(fishes[i][j][0]) # 물고기 번호
                fish_info[fishes[i][j][0]] = [i, j]
    # 물고기 번호순으로 정렬
    alive.sort()

    # 1번 물고기부터 이동
    # 물고기의 방향으로 이동할건데 상어가 있거나 경계를 넘으면 계속 45도씩 회전
    # 한바퀴 다 돌아도 갈 수 없으면 이동 안하고 그 물고기는 통과

    for num in alive:
        f_r, f_c = fish_info[num]
        direction = fishes[f_r][f_c][1]
        for k in range(8):
            new_dir = (direction + k) % 8
            nr = f_r + dr[new_dir]
            nc = f_c + dc[new_dir]
            if 0 <= nr < 4 and 0 <= nc < 4:
                if fishes[nr][nc] != -1: # 상어가 있는 칸이 아니면
                    if fishes[nr][nc] != 0: # 물고기가 있는 칸이면
                        fishes[f_r][f_c] = [num, new_dir]
                        fishes[f_r][f_c], fishes[nr][nc] = fishes[nr][nc], fishes[f_r][f_c]
                        fish_info[fishes[f_r][f_c][0]] = [f_r, f_c] # 딕셔너리에서 물고기 위치 수정
                        fish_info[fishes[nr][nc][0]] = [nr, nc] # 딕셔너리에서 물고기 위치 수정
                        break
                    else: # 빈칸일 경우
                        fishes[f_r][f_c] = [num, new_dir] # 빈칸일 경우에도 방향을 수정해서 도착한 것일 수 있으니깐 방향 업데이트.
                        fishes[f_r][f_c], fishes[nr][nc] = fishes[nr][nc], fishes[f_r][f_c]
                        fish_info[fishes[nr][nc][0]] = [nr, nc] # 딕셔너리에서 물고기 위치 수정
                        break
    return fishes

q = deque()
q.append((shark_r, shark_c, shark_d, eaten, board))

while q:
    s_r, s_c, s_d, total, fish = q.popleft()
    answer = max(answer, total)
    # 물고기 이동
    after_fish = fish_move(fish)


    # 상어 이동
    next_s_r = s_r
    next_s_c = s_c
    while True:
        next_s_r += dr[s_d]
        next_s_c += dc[s_d]
        if 0 <= next_s_r < 4 and 0 <= next_s_c < 4:
            # 물고기가 있는 칸이라면
            if after_fish[next_s_r][next_s_c] != -1 and after_fish[next_s_r][next_s_c] != 0:
                tmp = [next_s_r, next_s_c, after_fish[next_s_r][next_s_c][0], after_fish[next_s_r][next_s_c][1]]
                new_fish = deepcopy(after_fish)
                new_fish[s_r][s_c] = 0 # 기존에 상어가 있던 자리는 빈칸이 됨
                new_fish[next_s_r][next_s_c] = -1 # 새로운 자리로 상어 새로 이동
                q.append((next_s_r, next_s_c, tmp[3], total + tmp[2], new_fish))
            else:
                continue
        # 범위 벗어나면 그 이후로는 볼 필요 없음.
        else:
            break

print(answer)