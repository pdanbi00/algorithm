C, R = map(int, input().split())
K = int(input())
board = [[0] * C for _ in range(R)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r, c = R, 0

d = 0

if K > R * C:
    print(0)
else:
    idx = 1
    while idx <= K:
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == 0:
                board[nr][nc] = idx
                idx += 1
                r = nr
                c = nc
            else:
                d = (d + 1) % 4
        else:
            d = (d + 1) % 4
    print(nc+1, R-nr)