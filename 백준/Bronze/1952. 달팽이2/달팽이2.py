M, N = map(int, input().split())
board = [[-1] * N for _ in range(M)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ans = 0
board[0][0] = 0
r = c = 0
d = 0

while True:
    changed = False
    go = False
    for i in range(4):
        nr = r + dr[(d + i) % 4]
        nc = c + dc[(d + i) % 4]
        if nr < 0 or nr >= M or nc < 0 or nc >= N or board[nr][nc] != -1:
            changed = True
            continue
        go = True
        board[nr][nc] = 0
        r, c, d = nr, nc, (d + i) % 4
        break
    if changed and go:
        ans += 1
    if not go:
        break
print(ans)