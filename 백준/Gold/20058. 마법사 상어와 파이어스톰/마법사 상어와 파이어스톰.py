from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
N = 2 ** N
board = [list(map(int, input().split())) for _ in range(N)]
magic = list(map(int, input().split()))
total = 0
max_size = 0

# 격자 회전 시키기
 # 1. 판 2 ** l 크기로 나누기
    # 한 칸을 시계방향으로 90도 회전 시키기

# 격자 회전시키기
def move(r1, r2, c1, c2, n):
    arr = [[0] * N for _ in range(N)]
    s = 2 ** n
    for i in range((s//2)+1):
        # r1+i번째 행 채우기
        for si in range(s - (2*i)):
            arr[r1 + i][c1+i+si] = board[r2 - 1 - si - i][c1 + i]
        # c2-i-1번째 열 채우기
        for si in range(s - (2*i)):
            arr[r1+i+si][c2 - i - 1] = board[r1 + i][c1+i+si]
        # r2-i-1번째 행 채우기
        for si in range(s - (2*i)):
            arr[r2 - i - 1][c1+i+si] = board[r2 - si - 1 - i][c2 - i - 1]
        # c1+i번째 열 채우기
        for si in range(s - (2*i)):
            arr[r1+i+si][c1 + i] = board[r2 - i - 1][c1 + i + si]
    for i in range(r1, r2):
        for j in range(c1, c2):
            board[i][j] = arr[i][j]
# 격자 나누기
def divide(n):
    s = 2 ** n # 한 블록 크기
    for i in range(0, N, s):
        for j in range(0, N, s):
            move(i, i+s, j, j+s, n) # 격자 돌리기

# bfs
def bfs(i, j):
    global total, max_size
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    total += board[i][j]
    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] > 0 and visited[nr][nc] == 0:
                    cnt += 1
                    visited[nr][nc] = 1
                    total += board[nr][nc]
                    q.append((nr, nc))
    max_size = max(max_size, cnt)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for size in magic:
    # 격자판 나누고 회전시키기
    if size > 0:
        divide(size)

    ice = [] # 얼음 양 1 감소시켜야할 칸 정보

    # 회전 시킨 후 각 칸을 돌아다니면서 인접한 칸 3개 이상이 얼음 칸인지 확인
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                cnt = 0

                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if board[nr][nc] > 0:
                            cnt += 1
                if cnt < 3:
                    ice.append((i, j))
    # 아닐 경우 얼음 양 1 감소
    for ic in ice:
        board[ic[0]][ic[1]] -= 1

# 파이어스톰을 Q번 시전한 이후
visited = [[0] * N for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(N):
        # 방문하지 않은 모든 얼음 칸에 대해서
        if board[i][j] > 0 and visited[i][j] == 0:
            # bfs 돌면서 얼음양 모두 더하고, 연결되어 있는 칸 갯수 비교하기.
            bfs(i, j)

print(total)
print(max_size)