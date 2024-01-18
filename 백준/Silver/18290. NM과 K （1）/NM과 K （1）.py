N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
used = [[False] * M for _ in range(N)]
ans = -999999999
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def func(cnt, row, col, sum):
    if cnt == K:
        global ans
        if sum > ans:
            ans = sum
        return ans
    for i in range(row, N):
        for j in range(col if i == row else 0, M):
            if used[i][j]:
                continue
            possible = True
            for l in range(4):
                nx, ny = i+dx[l], j+dy[l]
                if 0 <= nx < N and 0 <= ny < M:
                    if used[nx][ny]:
                        possible = False
            if possible:
                used[i][j] = True
                func(cnt+1, i, j, sum+board[i][j])
                used[i][j] = False

func(0, 0, 0, 0)
print(ans)