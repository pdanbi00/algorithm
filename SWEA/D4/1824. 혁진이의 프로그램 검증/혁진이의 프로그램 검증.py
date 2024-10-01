from collections import deque
T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    memory = 0
    dr = [-1, 1, 0, 0] # 상하좌우
    dc = [0, 0, -1, 1]
    dir = 3
    r, c = 0, 0
    q = deque()
    q.append((r, c, dir, memory))
    visited = [[[[0] * C for _ in range(R)] for _ in range(16)] for _ in range(4)] # 상, 하, 좌, 우 방향 포함해서 방문 기록 남기기
    visited[dir][memory][r][c] = memory
    ans = False
    while q:
        r, c, dir, memory = q.popleft()
        if board[r][c] == '?':
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0:
                    nr = R - 1
                else:
                    nr = nr % R
                if nc < 0:
                    nc = C - 1
                else:
                    nc = nc % C
                if visited[i][memory][nr][nc] == 0:
                    q.append((nr, nc, i, memory))
                    visited[i][memory][nr][nc] = 1
        else:
            if board[r][c] == '<':
                dir = 2
            elif board[r][c] == '>':
                dir = 3
            elif board[r][c] == '^':
                dir = 0
            elif board[r][c] == 'v':
                dir = 1
            elif board[r][c] == '_':
                if memory == 0:
                    dir = 3
                else:
                    dir = 2
            elif board[r][c] == '|':
                if memory == 0:
                    dir = 1
                else:
                    dir = 0
            elif board[r][c] == '@':
                ans = True
                break
            elif board[r][c] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                memory = int(board[r][c])
            elif board[r][c] == '+':
                memory = (memory + 1) % 16
            elif board[r][c] == '-':
                memory -= 1
                if memory == -1:
                    memory = 15
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0:
                nr = R-1
            else:
                nr = nr % R
            if nc < 0:
                nc = C - 1
            else:
                nc = nc % C

            if visited[dir][memory][nr][nc] == 0:
                q.append((nr, nc, dir, memory))
                visited[dir][memory][nr][nc] = 1

    if ans:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')