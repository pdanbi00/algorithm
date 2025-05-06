from collections import deque

R, C = map(int, input().split())
board = []
for i in range(R):
    arr = list(input())
    for j in range(C):
        if arr[j] == 'M':
            m_r, m_c = i, j
        elif arr[j] == 'Z':
            z_r, z_c = i, j
    board.append(arr)

pipe = ['|', '-', '+', '1', '2', '3', '4']

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 모든 조건 다 나열해보세
def bfs():
    q = deque()
    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)] # 해당 하는 칸에 어떤 방향에서 들어왔는지도 기록
    for k in range(4):
        visited[m_r][m_c][k] = True
        nr = m_r + dr[k]
        nc = m_c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] in pipe:
                if k == 0:
                    if board[nr][nc] in ('|', '+', '1', '4'):
                        q.append((nr, nc, k))
                        visited[nr][nc][k] = True
                elif k == 1:
                    if board[nr][nc] in ('|', '+', '2', '3'):
                        q.append((nr, nc, k))
                        visited[nr][nc][k] = True
                elif k == 2:
                    if board[nr][nc] in ('-', '+', '1', '2'):
                        q.append((nr, nc, k))
                        visited[nr][nc][k] = True
                elif k == 3:
                    if board[nr][nc] in ('-', '+', '3', '4'):
                        q.append((nr, nc, k))
                        visited[nr][nc][k] = True

    while q:
        r, c, d = q.popleft()

        if board[r][c] == '|':
            # 아래쪽에서 온 경우
            if d == 0:
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('|', '+', '1', '4') and not visited[nr][nc][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = True

            # 위쪽에서 온 경우
            elif d == 1:
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('|', '+', '2', '3') and not visited[nr][nc][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = True

        elif board[r][c] == '-':
            # 오른쪽에서 온 경우
            if d == 2:
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True
                    if board[nr][nc] in ('-', '+', '1', '2') and not visited[nr][nc][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = True

            # 왼쪽에서 온 경우
            elif d == 3:
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('-', '+', '3', '4') and not visited[nr][nc][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = True

        elif board[r][c] == '+':
            # 아래쪽에서 온 경우
            if d == 0:
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('|', '+', '1', '4') and not visited[nr][nc][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = True
            # 위쪽에서 온 경우
            elif d == 1:
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('|', '+', '2', '3') and not visited[nr][nc][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = True

            # 오른쪽에서 온 경우
            elif d == 2:
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('-', '+', '1', '2') and not visited[nr][nc][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = True

            # 왼쪽에서 온 경우
            elif d == 3:
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('-', '+', '3', '4') and not visited[nr][nc][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = True

        elif board[r][c] == '1':
            # 오른쪽에서 온 경우
            if d == 2:
                nr = r + dr[1]
                nc = c + dc[1]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('|', '+', '2', '3') and not visited[nr][nc][1]:
                        q.append((nr, nc, 1))
                        visited[nr][nc][1] = True

            # 아래쪽에서 온 경우
            elif d == 0:
                nr = r + dr[3]
                nc = c + dc[3]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('-', '+', '3', '4') and not visited[nr][nc][3]:
                        q.append((nr, nc, 3))
                        visited[nr][nc][3] = True

        elif board[r][c] == '2':
            # 오른쪽에서 온 경우
            if d == 2:
                nr = r + dr[0]
                nc = c + dc[0]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('|', '+', '1', '4') and not visited[nr][nc][0]:
                        q.append((nr, nc, 0))
                        visited[nr][nc][0] = True

            # 위쪽에서 온 경우
            elif d == 1:
                nr = r + dr[3]
                nc = c + dc[3]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('-', '+', '3', '4') and not visited[nr][nc][3]:
                        q.append((nr, nc, 3))
                        visited[nr][nc][3] = True

        elif board[r][c] == '3':
            # 왼쪽에서 온 경우
            if d == 3:
                nr = r + dr[0]
                nc = c + dc[0]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('|', '+', '1', '4') and not visited[nr][nc][0]:
                        q.append((nr, nc, 0))
                        visited[nr][nc][0] = True

            # 위쪽에서 온 경우
            elif d == 1:
                nr = r + dr[2]
                nc = c + dc[2]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('-', '+', '1', '2') and not visited[nr][nc][2]:
                        q.append((nr, nc, 2))
                        visited[nr][nc][2] = True

        elif board[r][c] == '4':
            # 왼쪽에서 온 경우
            if d == 3:
                nr = r + dr[1]
                nc = c + dc[1]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('|', '+', '2', '3') and not visited[nr][nc][1]:
                        q.append((nr, nc, 1))
                        visited[nr][nc][1] = True

            # 아래쪽에서 온 경우
            elif d == 0:
                nr = r + dr[2]
                nc = c + dc[2]
                if 0 <= nr < R and 0 <= nc < C:
                    if nr == z_r and nc == z_c:
                        return True

                    if board[nr][nc] in ('-', '+', '1', '2') and not visited[nr][nc][2]:
                        q.append((nr, nc, 2))
                        visited[nr][nc][2] = True

    return False

for i in range(R):
    for j in range(C):
        if board[i][j] == '.':
            for k in range(7):
                board[i][j] = pipe[k]
                result = bfs()
                if result:
                    print(i+1, j+1, pipe[k])
                    exit()
            board[i][j] = '.'

