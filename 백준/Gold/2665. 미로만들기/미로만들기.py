from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

q = deque()
q.append((0, 0))
visited[0][0] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    r, c = q.popleft()
    
    if r == N-1 and c == N-1:
        break

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
            if board[nr][nc] == '1':
                q.appendleft((nr, nc))
                visited[nr][nc] = visited[r][c]
            elif board[nr][nc] == '0':
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

print(visited[N-1][N-1])