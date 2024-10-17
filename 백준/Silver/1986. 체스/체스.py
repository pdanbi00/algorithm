from collections import deque

N, M = map(int, input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))

# 체스판에 queen, knight, pawn 설치
board = [[0] * M for _ in range(N)]
if queen[0] != 0:
    for i in range(1, len(queen) - 1, 2):
        board[queen[i]-1][queen[i+1]-1] = 'Q'

if knight[0] != 0:
    for i in range(1, len(knight) - 1, 2):
        board[knight[i]-1][knight[i+1]-1] = 'K'

if pawn[0] != 0:
    for i in range(1, len(pawn) - 1, 2):
        board[pawn[i]-1][pawn[i+1]-1] = 'P'

def q_move(r, c):
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    for k in range(8):
        idx = 1
        while idx < max(N, M):
            nr = r + dr[k] * idx
            nc = c + dc[k] * idx
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 0 or board[nr][nc] == -1:
                    board[nr][nc] = -1
                    idx += 1
                else:
                    break
            else:
                break


def k_move(r, c):
    dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    dc = [-2, -1, 1, 2, 2, 1, -1, -2]

    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 0:
                board[nr][nc] = -1

for i in range(N):
    for j in range(M):
        if board[i][j] == 'Q':
            q_move(i, j)
        elif board[i][j] == 'K':
            k_move(i, j)
# print(board)
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            ans += 1
print(ans)