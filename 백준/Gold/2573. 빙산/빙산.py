from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

time = 0

def solve(i, j):
    # 빙하 찾기
    q = deque()
    q.append((i, j))
    ice = [(i, j)]
    melt = []
    visited[i][j] = True
    while q:
        r, c = q.popleft()
        cnt = 0 # 주변 얼음 개수
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and board[nr][nc] > 0:
                    q.append((nr, nc))
                    ice.append((nr, nc))
                    visited[nr][nc] = True
                elif board[nr][nc] == 0:
                    cnt += 1
        melt.append(cnt)

    # 빙하 녹이기
    for idx in range(len(ice)):
        r, c = ice[idx][0], ice[idx][1]
        board[r][c] -= melt[idx]
        if board[r][c] < 0:
            board[r][c] = 0
    # for i in range(N):
    #     print(board[i])
    # print('------------')


while True:
    cnt_bing = 0 # 빙하개수
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                cnt_bing += 1
                solve(i, j)
                # print(time)
    time += 1
    # print(cnt_bing)
    if cnt_bing >= 2:
        print(time-1)
        exit()
    elif cnt_bing == 0:
        print(0)
        exit()