import copy
N, M = map(int, input().split())
board = []
cctv = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    [[0, 1, 2, 3]]
]

# 북, 동, 남, 서 방향 순서 중요
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(M):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append((data[j], i, j))
# 감시
def fill(board, mode, r, c):
    for i in mode: # cctv 방향에 따라서
        nr = r
        nc = c
        while True:
            nr += dr[i]
            nc += dc[i]
            # 범위 넘어가면 중단
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                break
            # 벽이면 중단
            if board[nr][nc] == 6:
                break
            # 감시 가능하다면
            elif board[nr][nc] == 0:
                board[nr][nc] = -1

def dfs(depth, board):
    global min_value
    if depth == len(cctv): # 모든 cctv 다 확인한 경우
        count = 0
        # 사각지대 찾기
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    count += 1
        min_value = min(min_value, count)
        return
    temp = copy.deepcopy(board) # 보드 복사
    cctv_num, r, c = cctv[depth]
    for i in mode[cctv_num]: # cctv 방향에 따라서
        fill(temp, i, r, c)
        dfs(depth+1, temp)
        temp = copy.deepcopy(board)

min_value = 1e9
dfs(0, board)
print(min_value)