from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
zero = []
board = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j] == 0:
            zero.append((i, j))
    board.append(arr)

bfs_dict = dict()
visited = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

idx = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and visited[i][j] == 0:
            q = deque()
            q.append((i, j))
            visited[i][j] = idx
            cnt = 0
            while q:
                r, c = q.popleft()
                cnt += 1
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if board[nr][nc] == 1 and visited[nr][nc] == 0:
                            q.append((nr, nc))
                            visited[nr][nc] = idx
            bfs_dict[idx] = cnt
            idx += 1

ans = 0
for r, c in zero:
    used = []
    tmp = 1
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 1 and visited[nr][nc] not in used:
                used.append(visited[nr][nc])
                tmp += bfs_dict[visited[nr][nc]]

    ans = max(ans, tmp)

print(ans)