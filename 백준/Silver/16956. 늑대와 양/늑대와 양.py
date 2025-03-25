# 양의 상하좌우, 늑대의 상하좌우를 다 울타리를 설치.
from collections import deque
R, C = map(int, input().split())
targets = []
wolfs = []
board = []
for i in range(R):
    arr = list(input())
    for j in range(C):
        if arr[j] == '.':
            arr[j] = 'D'

        if arr[j] == 'W':
            wolfs.append((i, j))
    board.append(arr)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()
visited = [[False] * C for _ in range(R)]
for wolf in wolfs:
    q.append((wolf[0], wolf[1]))
    visited[wolf[0]][wolf[1]] = True

while q:
    r, c = q.popleft()
    if board[r][c] == 'S':
        print(0)
        exit()

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] != 'D' and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True

print(1)
for i in range(R):
    for j in range(C):
        print(board[i][j], end="")
    print()