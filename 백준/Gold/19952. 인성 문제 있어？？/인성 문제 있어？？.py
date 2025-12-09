from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, O, F, s_r, s_c, e_r, e_c = map(int, input().split())

    board = [[0] * W for _ in range(H)]

    for _ in range(O):
        r, c, h = map(int, input().split())
        board[r-1][c-1] = h

    visited = [[False] * W for _ in range(H)]

    q = deque()
    q.append((s_r-1, s_c-1, F))
    visited[s_r-1][s_c-1] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    possible = False
    while q:
        r, c, p = q.popleft()
        if r == e_r-1 and c == e_c-1:
            possible = True
            break

        if p <= 0:
            continue

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < H and 0 <= nc < W:
                if board[nr][nc] > board[r][c]:
                    if p >= board[nr][nc] - board[r][c] and not visited[nr][nc]:
                        q.append((nr, nc, p-1))
                        visited[nr][nc] = True
                else:
                    if not visited[nr][nc]:
                        q.append((nr, nc, p - 1))
                        visited[nr][nc] = True


    if possible:
        print("잘했어!!")
    else:
        print("인성 문제있어??")