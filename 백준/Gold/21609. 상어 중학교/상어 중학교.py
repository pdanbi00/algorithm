from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
score = 0

# 크기가 가장 큰 블록 찾는 함수
def find(): # 비교 기준 : 블록 총 개수 -> 포함된 무지개 블록 수 -> 기준 블록의 행이 가장 큰 것 -> 기준 블록의 열이 가장 큰 것
    global blockGroup, rainbowCnt, stdR, stdC
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                color = board[i][j]
                stR = i
                stC = j
                rainbow = 0
                blocks = []
                q = deque()
                visited = [[False] * N for _ in range(N)]
                q.append((i, j))
                blocks.append((i, j))
                visited[i][j] = True
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < N and 0 <= nc < N:
                            if (board[nr][nc] == color or board[nr][nc] == 0) and not visited[nr][nc]:
                                q.append((nr, nc))
                                visited[nr][nc] = True
                                blocks.append((nr, nc))
                                if board[nr][nc] == color:
                                    if nr < stR:
                                        stR = nr
                                        stC = nc
                                    elif nr == stR:
                                        if nc < stC:
                                            stC = nc
                                elif board[nr][nc] == 0:
                                    rainbow += 1
                if len(blocks) >= 2:
                    if (len(blocks) > len(blockGroup)) or (len(blocks) == len(blockGroup) and rainbow > rainbowCnt) or ((len(blocks) == len(blockGroup) and rainbow == rainbowCnt) and stR > stdR) or ((len(blocks) == len(blockGroup) and rainbow == rainbowCnt and stR == stdR) and stC > stdC):
                        blockGroup = blocks
                        rainbowCnt = rainbow
                        stdR = stR
                        stdC = stC

# 블록 제거 함수 : board값을 -2로 바꾸기
# find 에서 찾은 블록 그룹의 모든 블록을 제거. 제거한 블록 그룹에 호팜된 블록의 수의 제곱 만큼 점수 획득
def remove():
    global score
    score += len(blockGroup) * len(blockGroup)
    for r, c in blockGroup:
        board[r][c] = -2

# 중력 함수
def gravity():
    for j in range(N):
        for i in range(N-2, -1, -1):
            if board[i][j] >= 0:
                r = i
                while r < N-1:
                    if r+1 < N and board[r+1][j] == -2:
                        board[r+1][j] = board[r][j]
                        board[r][j] = -2
                        r += 1
                    else:
                        break

def rotation():
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = board[j][N-1-i]
    return arr


while True:
    blockGroup = [] # 가장 큰 블록 그룹에 속한 블록들
    rainbowCnt = 0 # 무지개 블럭록 개수
    stdR = -1 # 기준 블록 행
    stdC = -1 # 기준 블록 열
    find()
    if not blockGroup:
        break
    remove()
    gravity()
    board = rotation()
    gravity()

print(score)