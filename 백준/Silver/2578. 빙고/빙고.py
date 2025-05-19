board = []
bingo_info = dict()
for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        bingo_info[arr[j]] = (i, j)
    board.append(arr)

called = []
for _ in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        called.append(arr[j])

answer = 0

def check():
    line = 0
    # 행 확인하기
    for i in range(5):
        cnt = 0
        for j in range(5):
            if board[i][j] == 0:
                cnt += 1
        if cnt == 5:
            line += 1
    if line >= 3:
        return True

    # 열 확인하기
    for j in range(5):
        cnt = 0
        for i in range(5):
            if board[i][j] == 0:
                cnt += 1
        if cnt == 5:
            line += 1
    if line >= 3:
        return True

    # 오른쪽 아래 방향 대각선 확인하기
    cnt = 0
    for i in range(5):
        if board[i][i] == 0:
            cnt += 1
    if cnt == 5:
        line += 1

    if line >= 3:
        return True
    # 오른쪽 위 방향 대각선 확인하기
    cnt = 0
    for i in range(5):
        if board[i][4-i] == 0:
            cnt += 1
    if cnt == 5:
        line += 1

    if line >= 3:
        return True

    return False

for i in range(25):
    r, c = bingo_info[called[i]][0], bingo_info[called[i]][1]
    board[r][c] = 0
    answer += 1
    if check():
        print(answer)
        break