from collections import deque
M, N = map(int, input().split())
board = [list(input()) for _ in range(M)]

visited = [[False] * N for _ in range(M)]
q = deque()

for i in range(N):
    if board[0][i] == '0':
        q.append((0, i))
        visited[0][i] = True

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
possible = False

while q:
    r, c = q.popleft()
    if r == M-1:
        possible = True
        break

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < M and 0 <= nc < N:
            if board[nr][nc] == '0' and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True

if possible:
    print("YES")
else:
    print("NO")