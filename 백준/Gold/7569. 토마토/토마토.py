# 이건 백퍼 bfs
import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# visited =[[[-1]*M for _ in range(N)] for _ in range(H)]
dr = [0, 0, -1, 1, 0, 0] # 행
dc = [0, 0, 0, 0, -1, 1] # 열
dz = [-1, 1, 0, 0, 0, 0] # z축
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))


while q:
    z, r, c = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nz < H and 0 <= nr < N and 0 <= nc < M:
            if tomato[nz][nr][nc] == 0:
                q.append((nz, nr, nc))
                tomato[nz][nr][nc] = tomato[z][r][c] + 1
ans = 0
possible = True
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                possible = False
        ans = max(ans, max(tomato[i][j]))
if possible:
    print(ans-1)
else:
    print(-1)
