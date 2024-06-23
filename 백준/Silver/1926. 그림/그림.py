# bfs돌면서 최대 값 갱신
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]

max_ans = 0
def bfs(r, c):
    global max_ans
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    cnt = 1
    while q:
        cur_r, cur_c = q.popleft()
        for k in range(4):
            nr = cur_r + dr[k]
            nc = cur_c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 1 and visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    cnt += 1
    max_ans = max(max_ans, cnt)
ans_cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            ans_cnt += 1
print(ans_cnt)
print(max_ans)