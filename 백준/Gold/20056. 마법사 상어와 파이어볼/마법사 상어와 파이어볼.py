N, M, K = map(int, input().split())
fireball = []
for _ in range(M):
    # fireball.append(list(map(int, input().split())))
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    fireball.append((r, c, m, s, d))

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    global fireball
    board = [[[] for _ in range(N)] for _ in range(N)]
    new_fire = []
    for r, c, m, s, d in fireball:
        nr = (r + (dr[d] * s)) % N
        nc = (c + (dc[d] * s)) % N
        board[nr][nc].append((m, s, d))
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) == 1:
                m, s, d = board[i][j][0][0], board[i][j][0][1], board[i][j][0][2]
                new_fire.append((i, j, m, s, d))
            elif len(board[i][j]) >= 2:
                tmp_m, tmp_s, cnt_odd, cnt_even = 0, 0, 0, 0
                for m, s, d in board[i][j]:
                    tmp_m += m
                    tmp_s += s
                    if d % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1
                tmp_m //= 5
                if tmp_m > 0:
                    tmp_s //= len(board[i][j])
                    if cnt_even == len(board[i][j]) or cnt_odd == len(board[i][j]):
                        for p in (0, 2, 4, 6):
                            new_fire.append((i, j, tmp_m, tmp_s, p))
                    else:
                        for p in (1, 3, 5, 7):
                            new_fire.append((i, j, tmp_m, tmp_s, p))
    fireball = new_fire

for _ in range(K):
    move()
ans = 0
for ball in fireball:
    ans += ball[2]
print(ans)