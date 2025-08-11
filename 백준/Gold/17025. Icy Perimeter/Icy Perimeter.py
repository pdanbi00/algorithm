from collections import deque
N = int(input())
board = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer_line = 0
answer_cnt = 0

def bfs(r, c):
    q = deque()
    q.append((r, c))
    line = 0
    cnt = 1
    visited[r][c] = True
    while q:
        r, c = q.popleft()
        tmp = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == '#' and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    cnt += 1
                elif board[nr][nc] == '.':
                    tmp += 1
            else:
                tmp += 1
        line += tmp
    return (cnt, line)

for i in range(N):
    for j in range(N):
        if board[i][j] == '#' and not visited[i][j]:
            t, l = bfs(i, j)
            if t > answer_cnt:
                answer_cnt = t
                answer_line = l
            elif t == answer_cnt:
                if l < answer_line:
                    answer_line = l

print(answer_cnt, answer_line)