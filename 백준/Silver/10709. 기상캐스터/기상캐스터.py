from collections import deque

H, W = map(int, input().split())
board = []
q = deque()
visited = [[-1] * W for _ in range(H)]
for i in range(H):
    arr = list(input())
    for j in range(W):
        if arr[j] == 'c':
            visited[i][j] = 0
            q.append((i, j))
    board.append(arr)

while q:
    r, c = q.popleft()

    nr = r + 0
    nc = c + 1
    if 0 <= nr < H and 0 <= nc < W:
        if visited[nr][nc] == -1:
            q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1

for i in range(H):
    print(*visited[i])