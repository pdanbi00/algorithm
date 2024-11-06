R, C = map(int, input().split())
k = int(input())
board = [[0] * C for _ in range(R)]
for _ in range(k):
    br, bc = map(int, input().split())
    board[br][bc] = 1
rr, rc = map(int, input().split()) # 로봇 위치
directions = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dir = 0
board[rr][rc] = 1

while True:
    possible = False
    for k in range(4):
        n_dir = (dir + k) % 4
        d = directions[n_dir] - 1
        nr = rr + dr[d]
        nc = rc + dc[d]

        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == 0:
                board[nr][nc] = 1
                rr = nr
                rc = nc
                dir = n_dir
                possible = True
                break

    if not possible:
        break
print(rr, rc)