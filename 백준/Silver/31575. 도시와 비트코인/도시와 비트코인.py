from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

def bfs():
    dr = [0, 1]
    dc = [1, 0]

    q = deque()
    q.append((0, 0))
    visited = [[False] * N for _ in range(M)]
    visited[0][0] = True
    while q:
        r, c = q.popleft()
        if r == M-1 and c == N-1:
            return True

        for k in range(2):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < M and 0 <= nc < N:
                if board[nr][nc] == 1 and visited[nr][nc] == False:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    return False

if bfs():
    print("Yes")
else:
    print("No")