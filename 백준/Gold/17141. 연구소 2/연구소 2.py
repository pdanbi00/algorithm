from collections import deque
from itertools import combinations

N, M = map(int, input().split())
board = []
empty = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 2:
            empty.append((i, j))
    board.append(arr)

ans = 10000000

def bfs(virus):
    global ans
    arr = [[-1] * N for _ in range(N)]
    time = -1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    possible = True

    q = deque()
    # 바이러스 놓기
    for vi in virus:
        arr[vi[0]][vi[1]] = 0
        q.append((vi[0], vi[1]))
    # 바이러스 퍼지기
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] != 1 and arr[nr][nc] == -1:
                    q.append((nr, nc))
                    arr[nr][nc] = arr[r][c] + 1

    # 바이러스가 전체에 다 퍼졌는지 확인
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -1 and board[i][j] != 1:
                possible = False
                break
            else:
                time = max(time, arr[i][j])
        if not possible:
            break

    if possible:
        ans = min(time, ans)


for combi in combinations(empty, M):
    bfs(combi)
if ans == 10000000:
    print(-1)
else:
    print(ans)