from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
q = deque()
board = []
visited = [[1e9] * C for _ in range(R)]

for i in range(R):
    arr = list(map(int, input().split()))
    if i == 0:
        for j in range(C):
            if arr[j] == 1:
                q.append((i, j))
                visited[i][j] = 0
    board.append(arr)

N = int(input())
dx = []

for _ in range(N):
    r, c = map(int, input().split())
    dx.append((r, c))

answer = 1e9
while q:
    r, c = q.popleft()
    if r == R-1:
        answer = visited[r][c]
        break

    for k in range(N):
        nr = r + dx[k][0]
        nc = c + dx[k][1]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == 1 and visited[nr][nc] == 1e9:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
if answer == 1e9:
    print(-1)
else:
    print(answer)