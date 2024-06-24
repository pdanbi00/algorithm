from collections import deque
# 3차원 bfs
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]


def bfs(z, r, c, visited):
    global ans
    q = deque()
    q.append((z, r, c))
    visited[z][r][c] = 0
    while q:
        cur_z, cur_r, cur_c = q.popleft()
        if board[cur_z][cur_r][cur_c] == 'E':
            ans = visited[cur_z][cur_r][cur_c]
            break
        for k in range(6):
            next_z = cur_z + dz[k]
            next_r = cur_r + dr[k]
            next_c = cur_c + dc[k]
            if 0 <= next_z < L and 0 <= next_r < R and 0 <= next_c < C:
                if board[next_z][next_r][next_c] != '#' and visited[next_z][next_r][next_c] == -1:
                    q.append((next_z, next_r, next_c))
                    visited[next_z][next_r][next_c] = visited[cur_z][cur_r][cur_c] + 1


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    board = []
    for _ in range(L):
        board.append([list(input()) for _ in range(R)])
        blank = list(input())
    # print(board)
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    ans = -1
    for i in range(L):
        for j in range(R):
            for p in range(C):
                if board[i][j][p] == 'S':
                    bfs(i, j, p, visited)
    if ans == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {ans} minute(s).')