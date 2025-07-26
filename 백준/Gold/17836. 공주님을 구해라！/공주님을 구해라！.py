from collections import deque
N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()
visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
q.append((0, 0, 0)) # r, c, 칼 여부
visited[0][0][0] = 0
answer = 1e9
while q:
    r, c, s = q.popleft()
    if r == N-1 and c == M-1:
        answer = visited[r][c][s]
        break

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if s:
                if visited[nr][nc][s] == -1:
                    q.append((nr, nc, s))
                    visited[nr][nc][s] = visited[r][c][s] + 1
            else:
                if board[nr][nc] == 0 and visited[nr][nc][s] == -1:
                    q.append((nr, nc, s))
                    visited[nr][nc][s] = visited[r][c][s] + 1
                elif board[nr][nc] == 2 and visited[nr][nc][1] == -1:
                    q.append((nr, nc, 1))
                    q.append((nr, nc, 0))
                    visited[nr][nc][1] = visited[r][c][s] + 1
                    visited[nr][nc][s] = visited[r][c][s] + 1

if answer <= T:
    print(answer)

else:
    print("Fail")