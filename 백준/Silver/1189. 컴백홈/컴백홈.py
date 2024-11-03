import sys
input = sys.stdin.readline
R, C, K = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]
# board[R-1][0] = 'S'
# board[0][C-1] = 'E'

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0

def dfs(r, c, depth):
    global cnt
    if r == 0 and c == C-1 and depth == K:
        cnt += 1
    else:
        board[r][c] = 'T'
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] == '.':
                    board[nr][nc] = 'T'
                    dfs(nr, nc, depth+1)
                    board[nr][nc] = '.'

dfs(R-1, 0, 1)
print(cnt)