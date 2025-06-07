M, N = map(int, input().split())
board = [[1] * M for _ in range(M)]

for _ in range(N):
    cnt = list(map(int, input().split()))
    big = [0] * cnt[0] + [1] * cnt[1] + [2] * cnt[2]
    visited = [[0] * M for  _ in range(M)]
    idx = 0
    r = M-1
    c = 0
    while idx < len(big):
        if r > 0:
            visited[r][c] = big[idx]
            idx += 1
            r -= 1
        else:
            visited[r][c] = big[idx]
            c += 1
            idx += 1
    dr = [0, -1, -1]
    dc = [-1, -1, 0]

    for i in range(1, M):
        for j in range(1, M):
            for k in range(3):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < M and 0 <= nc < M:
                    visited[i][j] = max(visited[i][j], visited[nr][nc])
    # for i in range(M):
    #     print(*visited[i])
    # print('--------------')
    for i in range(M):
        for j in range(M):
            board[i][j] += visited[i][j]

for i in range(M):
    print(*board[i])