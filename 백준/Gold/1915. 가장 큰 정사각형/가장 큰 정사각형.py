# import sys
# input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        if i > 0 and j > 0 and board[i][j] == 1:
            board[i][j] += min(board[i-1][j-1], board[i-1][j], board[i][j-1])
        ans = max(ans, board[i][j])
print(ans ** 2)
'''
5 4
0100
0111
1111
1111
0010
'''