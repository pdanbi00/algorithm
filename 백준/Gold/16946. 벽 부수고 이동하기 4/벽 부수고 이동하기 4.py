# 인접하는 0들을 그룹으로 표시
# 각 그룹에 0이 몇개씩 있는지 딕셔너리에 기록해두기
# 벽에서 상하좌우로 인접한 그룹 구해서 각 그룹에 해당하는 0 개수 더하기

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
zero = [[0] * M for _ in range(N)]

group = 1
info = {}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    zero[i][j] = group
    cnt = 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 0 and not visited[nr][nc]:
                    cnt += 1
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    zero[nr][nc] = group
    return cnt

# 인접하는 0들을 그룹으로 표시
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not visited[i][j]:
            w = bfs(i, j)
            # 각 그룹에 0이 몇개씩 있는지 딕셔너리에 기록해두기
            info[group] = w
            group += 1

# 벽에서 상하좌우로 인접한 그룹 구해서 각 그룹에 해당하는 0 개수 더하기
for i in range(N):
    for j in range(M):
        addList = set()
        if board[i][j] == 1:
            for k in range(4):
                ni = i + dr[k]
                nj = j + dc[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if zero[ni][nj] != 0:
                        addList.add(zero[ni][nj])
            for a in addList:
                board[i][j] += info[a]
                board[i][j] %= 10

for i in range(N):
    print(''.join(map(str, board[i])))