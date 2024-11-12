from collections import deque
R, C, T = map(int, input().split())
board = []
machine = []
for i in range(R):
    arr = list(map(int, input().split()))
    for j in range(C):
        if arr[j] == -1:
            machine.append(i)
            break
    board.append(arr)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 확산시키기
def spread():
    q = deque()
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                q.append((i, j, board[i][j] // 5))

    while q:
        r, c, dust = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                board[nr][nc] += dust
                board[r][c] -= dust

def clean():
    # 위쪽 공기청정기(반시계방향으로 순환)
    # 0행 왼쪽으로 한칸씩 옮기기
    tmp = board[0][0]
    for j in range(C-1):
        board[0][j] = board[0][j+1]

    # 0열 아래쪽으로 한칸씩 옮기기
    for i in range(machine[0]-1, 1, -1):
        board[i][0] = board[i-1][0]
    board[1][0] = tmp

    # 위쪽 청정기 있는 행 오른쪽으로 한칸씩 옮기기
    tmp = board[machine[0]][C-1]
    for j in range(C-1, 1, -1):
        board[machine[0]][j] = board[machine[0]][j-1]
    board[machine[0]][1] = 0

    # 마지막 열 위쪽으로 한칸씩 옮기기
    for i in range(machine[0]-1):
        board[i][C-1] = board[i+1][C-1]
    board[machine[0]-1][C-1] = tmp

    #######################################
    # 아래쪽 공기청정기(시계방향으로 순환)
    # 마지막행 왼쪽으로 한칸씩 옮기기
    tmp = board[R-1][0]
    for j in range(C - 1):
        board[R-1][j] = board[R-1][j + 1]

    # 0열 위쪽으로 한칸씩 옮기기
    for i in range(machine[1]+1, R-1):
        board[i][0] = board[i+1][0]
    board[R-1-1][0] = tmp

    # 아래쪽 청정기 있는 행 오른쪽으로 한칸씩 옮기기
    tmp = board[machine[1]][C - 1]
    for j in range(C - 1, 1, -1):
        board[machine[1]][j] = board[machine[1]][j - 1]
    board[machine[1]][1] = 0

    # 마지막 열 아래쪽으로 한칸씩 옮기기
    for i in range(R - 1, machine[1], -1):
        board[i][C - 1] = board[i - 1][C - 1]
    board[machine[1]+1][C - 1] = tmp

time = 0
while time < T:
    spread()
    # for i in range(R):
    #     print(board[i])
    # print('-------------')
    clean()
    # for i in range(R):
    #     print(board[i])
    # print('-------------')
    time += 1
    if time == T:
        # print(board)
        answer = 0
        for i in range(R):
            for j in range(C):
                if board[i][j] > 0:
                    answer += board[i][j]
print(answer)

'''
3 3 1
0 30 7
-1 10 0
-1 0 20
'''