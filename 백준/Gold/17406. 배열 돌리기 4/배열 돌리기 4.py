from copy import deepcopy
from itertools import permutations
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 1e9
move = [list(map(int, input().split())) for _ in range(K)]
for perm in permutations(move):
    board_copy = deepcopy(board)
    for r, c, s in perm:
        r -= 1 # 인덱스 맞추려고
        c -= 1 # 인덱스 맞추려고

        for n in range(s, 0, -1):
            temp = board_copy[r-n][c+n]
            board_copy[r-n][c-n+1:c+n+1] = board_copy[r-n][c-n:c+n]
            for row in range(r-n, r+n):
                board_copy[row][c-n] = board_copy[row+1][c-n]
            board_copy[r+n][c-n:c+n] = board_copy[r+n][c-n+1:c+n+1]
            for row in range(r+n, r-n, -1):
                board_copy[row][c+n] = board_copy[row-1][c+n]
            board_copy[r-n+1][c+n] = temp
    for i in board_copy:
        answer = min(answer, sum(i))
print(answer)