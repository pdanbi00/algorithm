# 0 : 청소 되지 않은 상태   1 : 벽   2 : 청소 한 상태
N, M = map(int, input().split())
r, c, d = map(int, input().split())
# d -> 0: 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0 # 청소한 칸 수
while True:
    # 현재 칸이 청소 안 되어 있으면 청소한다.
    if board[r][c] == 0:
        board[r][c] = 2
        ans += 1
    # 현재 칸 주변 4칸이 다 청소된 상태면
    if board[r-1][c] != 0 and board[r][c+1] != 0 and board[r+1][c] != 0 and board[r][c-1] != 0:
        if board[r-dr[d]][c-dc[d]] == 1: # 후진할 수 없으면 작동 멈춤
           break
        else:
            r -= dr[d]
            c -= dc[d]
    # 현재 칸 주변 4칸 중 청소하지 않은 빈칸이 있으면
    else:
        d = (d+3) % 4 # 원래는 d-1 을 해야하는데 그럼 d가 0이면 -1이니깐 +4 해서 +3이 됨
        if board[r+dr[d]][c+dc[d]] == 0:
            r += dr[d]
            c += dc[d]
print(ans)
