# 원래 비활성화였던 바이러스는 스스로 퍼져나갈 수 없음.
# 즉, 활성 상태 바이러스가 비활성 상태인 바이러스를 타고 넘어가서 이동

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 1000000000000


# 벽은 '-', 바이러스 위치는 '*'(비활성화), 나머지는 -1로 초기화
# 바이러스 위치가 담긴 큐를 return
def init():
    virus = deque()
    for i in range(N):
        for j in range(N):
            # 벽일 경우
            if board[i][j] == 1:
                board[i][j] = '-'
            elif board[i][j] == 2:
                board[i][j] = '*'
                virus.append((i, j))
            else:
                board[i][j] = -1
    return virus

viruses = init()

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
                if board[nr][nc] != '-' and visited[nr][nc] == -1:
                    if board[nr][nc] == -1:
                        visited[nr][nc] = visited[r][c] + 1
                        time = max(time, visited[nr][nc])
                    # 비활성화 상태의 바이러스를 만나면 통과해야 하기 때문에 시간은 1초 늘리지만 갱신은 안함
                    elif board[nr][nc] == '*':
                        visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

    for i in range(N):
        for j in range(N):
            if board[i][j] == -1 and visited[i][j] == -1:
                time = 1000000000000
                return time
    return time

for combi in combinations(viruses, M):
    # print(combi)
    ans = min(bfs(combi), ans)
    # for i in range(N):
    #     print(board[i])
    # print('---------')
if ans == 1000000000000:
    print(-1)
else:
    print(ans)