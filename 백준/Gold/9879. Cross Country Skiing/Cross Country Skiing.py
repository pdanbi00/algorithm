from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
board = []
max_v = 0
min_v = 1e10
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(M):
    arr = list(map(int, input().split()))
    for j in range(N):
        max_v = max(max_v, arr[j])
        min_v = min(min_v, arr[j])
    board.append(arr)

points = []
for i in range(M):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 1:
            points.append((i, j))

s_r = points[0][0]
s_c = points[0][1]

def bfs(r, c, d):
    q = deque()
    q.append((r, c))
    visited = [[False] * N for _ in range(M)]
    visited[r][c] = True
    cnt = 1
    while q:
        rr, cc = q.popleft()
        for k in range(4):
            nr = rr + dr[k]
            nc = cc + dc[k]
            if (0 <= nr < M and 0 <= nc < N):
                if (abs(board[rr][cc] - board[nr][nc]) <= d and not visited[nr][nc]):
                    q.append((nr, nc))
                    visited[nr][nc] = True

    for r, c in points:
        if not visited[r][c]:
            return False
    return True

left = 0
right = max_v - min_v
ans = -1
while left <= right:
    mid = (left + right) // 2
    if bfs(s_r, s_c, mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
