from collections import deque
K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

# 원숭이로 상하좌우
m_dr = [-1, 1, 0, 0]
m_dc = [0, 0, -1, 1]

# 말로 상하좌우
h_dr = [-2, -2, -1, -1, 1, 1, 2, 2]
h_dc = [-1, 1, -2, 2, -2, 2, -1, 1]

visited = [[[-1] * (K+1) for _ in range(W)] for _ in range(H)]

def bfs():
    q = deque()
    q.append((0, 0, 0)) # (행, 열, 말처럼 이동한 횟수)
    visited[0][0][0] = 0

    while q:
        r, c, z = q.popleft()
        if r == H-1 and c == W-1:
            print(visited[r][c][z])
            return
        for k in range(8): # 말처럼 이동하는거
            nr = r + h_dr[k]
            nc = c + h_dc[k]
            if 0 <= nr < H and 0 <= nc < W:
                if board[nr][nc] == 0 and z < K and visited[nr][nc][z+1] == -1:
                    q.append((nr, nc, z+1))
                    visited[nr][nc][z+1] = visited[r][c][z] + 1
        for k in range(4): # 원숭이로 이동하는거
            m_nr = r + m_dr[k]
            m_nc = c + m_dc[k]
            if 0 <= m_nr < H and 0 <= m_nc < W:
                if board[m_nr][m_nc] == 0 and visited[m_nr][m_nc][z] == -1:
                    q.append((m_nr, m_nc, z))
                    visited[m_nr][m_nc][z] = visited[r][c][z] + 1
    print(-1)
    return

bfs()
