# 오른쪽, 아래쪽, 오른쪽 아래 대각선 확인
# 딱 5개만 있어야 됨
# 검은색 이기면 1, 흰색 이기면 2, 결정 안났으면 0
# 검은색이나 흰색이 이겼으면 제일 왼쪽 혹은 제일 위 행, 열 좌표 출력
from collections import deque
board = [list(map(int, input().split())) for _ in range(19)]
visited = [[[0, 0, 0, 0] for _ in range(19)] for _ in range(19)]
dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1]
find_ans = False
def bfs(i, j, k, col):
    cnt = 1
    q = deque()
    q.append((i, j, k))
    visited[i][j][k] = 1
    while q:
        r, c, k = q.popleft()
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < 19 and 0 <= nc < 19:
            if visited[nr][nc][k] == 0 and board[nr][nc] == col:
                cnt += 1
                q.append((nr, nc, k))
                visited[nr][nc][k] = 1
    return cnt
col = 0
for i in range(19):
    for j in range(19):
        col = board[i][j]
        if col > 0:
            for k in range(4):
                ni = i + dr[k]
                nj = j + dc[k]
                if 0 <= ni < 19 and 0 <= nj < 19:
                    if board[ni][nj] == col:
                        c = bfs(i, j, k, col)
                        if c == 5:
                            if k == 3:
                                print(col)
                                print(i+5, j-3)
                            else:
                                print(col)
                                print(i+1, j+1)
                            find_ans = True
                            exit()
if not find_ans:
    print(0)
