N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# dfs
# 우선 해당 방향으로 다 이동시킴.
# 합칠 수 있는 것들 합치기
# 합친 후에 다시 해당 방향으로 다 이동시키기

def move_up(N, board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[i][j]

    for i in range(1, N):
        for j in range(N):
            if new_board[i][j] != 0:
                idx = i-1
                while idx >= 0:
                    if new_board[idx][j] == 0:
                        idx -= 1
                    else:
                        break
                if new_board[idx+1][j] == 0:
                    new_board[idx+1][j] = new_board[i][j]
                    new_board[i][j] = 0

    return new_board


def move_down(N, board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[i][j]
    for i in range(N-2, -1, -1):
        for j in range(N):
            if new_board[i][j] != 0:
                idx = i+1
                while idx < N:
                    if new_board[idx][j] == 0:
                        idx += 1
                    else:
                        break
                if new_board[idx-1][j] == 0:
                    new_board[idx-1][j] = new_board[i][j]
                    new_board[i][j] = 0
    return new_board

def move_right(N, board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[i][j]
    for j in range(N-2, -1, -1):
        for i in range(N):
            if new_board[i][j] != 0:
                idx = j+1
                while idx < N:
                    if new_board[i][idx] == 0:
                        idx += 1
                    else:
                        break
                if new_board[i][idx-1] == 0:
                    new_board[i][idx-1] = new_board[i][j]
                    new_board[i][j] = 0
    return new_board

def move_left(N, board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[i][j]

    for j in range(1, N):
        for i in range(N):
            if new_board[i][j] != 0:
                idx = j-1
                while idx >= 0:
                    if new_board[i][idx] == 0:
                        idx -= 1
                    else:
                        break
                if new_board[i][idx+1] == 0:
                    new_board[i][idx+1] = new_board[i][j]
                    new_board[i][j] = 0
    return new_board

def add_up(N, arr):
    global ans
    for j in range(N):
        idx = 0
        while idx < N-1:
            if arr[idx][j] != 0 and arr[idx][j] == arr[idx+1][j]:
                arr[idx][j] = arr[idx][j] * 2
                ans = max(ans, arr[idx][j])
                arr[idx+1][j] = 0
                idx += 2
            else:
                idx += 1
    return arr

def add_down(N, arr):
    for j in range(N):
        idx = N-1
        while idx > 0:
            if arr[idx][j] != 0 and arr[idx][j] == arr[idx-1][j]:
                arr[idx][j] = arr[idx][j] * 2
                arr[idx-1][j] = 0
                idx -= 2
            else:
                idx -= 1
    return arr

def add_right(N, arr):
    for i in range(N):
        idx = N-1
        while idx > 0:
            if arr[i][idx] != 0 and arr[i][idx] == arr[i][idx-1]:
                arr[i][idx] = arr[i][idx] * 2
                arr[i][idx-1] = 0
                idx -= 2
            else:
                idx -= 1
    return arr

def add_left(N, arr):
    for i in range(N):
        idx = 0
        while idx < N-1:
            if arr[i][idx] != 0 and arr[i][idx] == arr[i][idx+1]:
                arr[i][idx] = arr[i][idx] * 2
                arr[i][idx+1] = 0
                idx += 2
            else:
                idx += 1
    return arr

def up(N, board):
    arr = move_up(N, board)
    arr = add_up(N, arr)
    arr = move_up(N, arr)
    return arr

def down(N, board):
    arr = move_down(N, board)
    arr = add_down(N, arr)
    arr = move_down(N, arr)
    return arr

def left(N, board):
    arr = move_left(N, board)
    arr = add_left(N, arr)
    arr = move_left(N, arr)
    return arr

def right(N, board):
    arr = move_right(N, board)
    arr = add_right(N, arr)
    arr = move_right(N, arr)
    return arr

ans = 0
def dfs(N, board, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j])
        # for i in range(N):
        #     print(board[i])
        # print('--------------')
        return


    new_arr = up(N, board)
    dfs(N, new_arr, cnt+1)

    new_arr = down(N, board)
    dfs(N, new_arr, cnt + 1)

    new_arr = left(N, board)
    dfs(N, new_arr, cnt + 1)


    new_arr = right(N, board)
    dfs(N, new_arr, cnt + 1)

dfs(N, board, 0)
print(ans)