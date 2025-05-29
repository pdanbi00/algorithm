import sys
sys.setrecursionlimit(10**9)
T = int(input())
dr = [0, 1] # 오른쪽, 아래쪽
dc = [1, 0]

def func(cnt, r, c, d):
    if r == N-1 and c == N-1:
        return 1

    if dp[r][c][cnt][d] != -1:
        return dp[r][c][cnt][d]

    # 가능한 경로 수
    ret = 0

    if cnt <= K:
        for k in range(2):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] != 'H':
                    if d != k:
                        ret += func(cnt+1, nr, nc, k)
                    else:
                        ret += func(cnt, nr, nc, k)
    elif cnt == K+1:
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] != 'H':
                ret += func(cnt, nr, nc, d)


    dp[r][c][cnt][d] = ret
    return dp[r][c][cnt][d]

for _ in range(T):
    N, K = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    dp = [[[[-1] * 3 for _ in range(K+2)] for _ in range(N)] for _ in range(N)]
    path_set = set()

    print(func(0, 0, 0, 2))