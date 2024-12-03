# 원래 비활성화였던 바이러스는 스스로 퍼져나갈 수 없음.
# 즉, 활성 상태 바이러스가 비활성 상태인 바이러스를 타고 넘어가서 이동

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
board = []
virus = []

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 2:
            virus.append((i, j))
    board.append(arr)

ans = 1000000000000

def bfs(vir):
    global ans
    visited = [[-1] * N for _ in range(N)]

    q = deque()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    time = 0

    # 바이러스 활성화
    for vi in vir:
        visited[vi[0]][vi[1]] = 0
        q.append((vi[0], vi[1]))

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] != 1 and visited[nr][nc] == -1:
                    if board[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] + 1
                        time = max(time, visited[nr][nc])
                    # 비활성화 상태의 바이러스를 만나면 통과해야 하기 때문에 시간은 1초 늘리지만 갱신은 안함
                    elif board[nr][nc] == 2:
                        visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and visited[i][j] == -1:
                time = 1000000000000
                return time
    return time

for combi in combinations(virus, M):
    ans = min(bfs(combi), ans)

if ans == 1000000000000:
    print(-1)
else:
    print(ans)