# 다음 칸이 벽이면 이동 안함
# 다음 칸이 범위 밖이면 동전은 바닥으로 떨어짐.(board에서 없애면 됨)
# 이동하는 칸에 동전 있어도 감.

# 두 동전 중 하나만 보드에서 떨어뜨리기 위해서는 버튼 최소 몇 번 눌러야하는지 구해야 됨.

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

coins = []
ans = [1e9, N, M] # 이동한 횟수, 행, 열

def move(coins, idx): # 동전들 위치, 몇번째 이동인지,
    global ans
    if idx == 10:
        if len(coins) == 1:
            if idx < ans[0]:
                ans = [idx, coins[0][0], coins[0][1]]
        return
    elif idx < 10:
        if len(coins) == 1:
            if idx < ans[0]:
                ans = [idx, coins[0][0], coins[0][1]]
            return
        for k in range(4):
            tmp = []
            for coin in coins:
                nr = coin[0] + dr[k]
                nc = coin[1] + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    if board[nr][nc] != '#':
                        tmp.append((nr, nc))
                    else:
                        tmp.append((coin[0], coin[1]))
            if len(tmp) >= 1:
                move(tmp, idx+1)
        return



for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

move(coins, 0)

if ans[0] == 1e9:
    print(-1)
else:
    print(ans[0])