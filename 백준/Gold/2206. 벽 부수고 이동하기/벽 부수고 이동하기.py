from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# visited[i][j][0] : 벽을 아직 하나도 부수지 않고 i행 j열에 도착
# visited[i][j][1] : 벽을 하나 부순 상태로만 i행 j열에 도착

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        r, c, z = q.popleft()
        if r == N-1 and c == M-1:
            print(visited[r][c][z])
            return
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                # 다음으로 이동할 곳이 벽이고, 벽을 아직 부수지 않은 경우
                if board[nr][nc] == 1 and z == 0:
                    q.append((nr, nc, 1))
                    visited[nr][nc][1] = visited[r][c][0] + 1
                # 다음으로 이동할 곳이 벽이 아니고, 아직 방문 안했을 경우
                elif board[nr][nc] == 0 and visited[nr][nc][z] == 0:
                    q.append((nr, nc, z))
                    visited[nr][nc][z] = visited[r][c][z] + 1

    print(-1)
    return

bfs()
