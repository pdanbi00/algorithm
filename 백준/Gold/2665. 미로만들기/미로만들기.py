from collections import deque
N = int(input())
board = [list(input()) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

q = deque()
q.append((0, 0))
visited[0][0] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    r, c = q.popleft()

    if r == N-1 and c == N-1:
        continue

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == '1' and (visited[nr][nc] == -1 or visited[nr][nc] > visited[r][c]):
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c]
            elif board[nr][nc] == '0' and (visited[nr][nc] == -1 or visited[nr][nc] > visited[r][c] + 1):
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

# for i in range(N):
#     print(visited[i])
print(visited[N-1][N-1])