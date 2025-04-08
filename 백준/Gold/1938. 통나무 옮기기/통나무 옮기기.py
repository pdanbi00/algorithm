from collections import deque
from copy import deepcopy
N = int(input())
board = []
tong = []
target = []
for i in range(N):
    arr = list(input())
    for j in range(N):
        if arr[j] == 'B':
            tong.append([i, j])
        elif arr[j] == 'E':
            target.append([i, j])
    board.append(arr)

# 통나무 방향 판단하기
if tong[0][0] == tong[1][0]: # 가로
    tong.append(0)
else: # 세로
    tong.append(1)

# 상하좌우 움직이기 가능
# 이동하려는 곳이 1이 아니어야 됨
# visited에 통나무 위치 배열 계속 담기
# 이동할 때마다 방향도 기록해놓기
# 가로 방향일 경우 회전시키려면 상하에 1이 없어야 됨
# 세로 방향일 경우 회전시키려면 좌우에 1이 없어야 됨

# 통나무가 가로일 경우 상, 하, 좌, 우, 회전 확인
def garo(tree, cnt):
    global q, visited

    # 상
    possible = True
    t = deepcopy(tree[:3])
    for k in range(3):
        if t[k][0] - 1 < 0 or board[t[k][0] - 1][t[k][1]] == '1':
            possible = False
    if possible:
        for k in range(3):
            t[k][0] -= 1
        if t not in visited:
            q.append([t + [0], cnt + 1])
            visited.append(t)

    # 하
    possible = True
    t = deepcopy(tree[:3])
    for k in range(3):
        if t[k][0] + 1 >= N or board[t[k][0] + 1][t[k][1]] == '1':
            possible = False
    if possible:
        for k in range(3):
            t[k][0] += 1
        if t not in visited:
            q.append([t + [0], cnt + 1])
            visited.append(t)

    # 좌
    possible = True
    t = deepcopy(tree[:3])
    if t[0][1] - 1 < 0 or board[t[0][0]][t[0][1] - 1] == '1':
        possible = False
    if possible:
        for k in range(3):
            t[k][1] -= 1
        if t not in visited:
            q.append([t + [0], cnt + 1])
            visited.append(t)
    # 우
    possible = True
    t = deepcopy(tree[:3])
    if t[2][1] + 1 >= N or board[t[2][0]][t[2][1] + 1] == '1':
        possible = False
    if possible:
        for k in range(3):
            t[k][1] += 1
        if t not in visited:
            q.append([t + [0], cnt + 1])
            visited.append(t)
    # 회전
    possible = True
    t = deepcopy(tree[:3])
    for k in range(3):
        if t[k][0] + 1 >= N or board[t[k][0] + 1][t[k][1]] == '1' or t[k][0] - 1 < 0 or board[t[k][0] - 1][t[k][1]] == '1':
            possible = False
    if possible:
        t = [[t[1][0] - 1 , t[1][1]], [t[1][0] , t[1][1]], [t[1][0] + 1 , t[1][1]]]
        if t not in visited:
            q.append([t + [1], cnt + 1])
            visited.append(t)

# 통나무가 세로일 경우 상, 하, 좌, 우, 회전 확인
def sero(tree, cnt):
    global q, visited
    # 상
    possible = True
    t = deepcopy(tree[:3])
    if t[0][0] - 1 < 0 or board[t[0][0]-1][t[0][1]] == '1':
        possible = False
    if possible:
        for k in range(3):
            t[k][0] -= 1
        if t not in visited:
            q.append([t + [1], cnt + 1])
            visited.append(t)

    # 하
    possible = True
    t = deepcopy(tree[:3])
    if t[2][0] + 1 >= N or board[t[2][0] + 1][t[2][1]] == '1':
        possible = False
    if possible:
        for k in range(3):
            t[k][0] += 1
        if t not in visited:
            q.append([t + [1], cnt + 1])
            visited.append(t)

    # 좌
    possible = True
    t = deepcopy(tree[:3])
    for k in range(3):
        if t[k][1] - 1 < 0 or board[t[k][0]][t[k][1] - 1] == '1':
            possible = False
    if possible:
        for k in range(3):
            t[k][1] -= 1
        if t not in visited:
            q.append([t + [1], cnt + 1])
            visited.append(t)

    # 우
    possible = True
    t = deepcopy(tree[:3])
    for k in range(3):
        if t[k][1] + 1 >= N or board[t[k][0]][t[k][1] + 1] == '1':
            possible = False
    if possible:
        for k in range(3):
            t[k][1] += 1
        if t not in visited:
            q.append([t + [1], cnt + 1])
            visited.append(t)

    # 회전
    possible = True
    t = deepcopy(tree[:3])
    for k in range(3):
        if t[k][1] + 1 >= N or board[t[k][0]][t[k][1] + 1] == '1' or t[k][1] - 1 < 0 or board[t[k][0]][t[k][1] - 1] == '1':
            possible = False
    if possible:
        t = [[t[1][0], t[1][1] - 1], [t[1][0], t[1][1]], [t[1][0], t[1][1] + 1]]
        if t not in visited:
            q.append([t + [0], cnt + 1])
            visited.append(t)

answer = 1e9
visited = []
q = deque()
q.append([tong, 0]) # [나무 위치들, 방향], 움직인 횟수
visited.append(tong[:-1])
while q:
    tree, cnt = q.popleft()
    # print(tree)
    if tree[0] == target[0] and tree[1] == target[1] and tree[2] == target[2]:
        answer = cnt
        break
    if tree[-1] == 0:
        garo(tree, cnt)
    else:
        sero(tree, cnt)

if answer == 1e9:
    print(0)
else:
    print(answer)