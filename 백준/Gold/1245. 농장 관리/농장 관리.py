from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

cnt = 0

def bfs(i, j):
    global flag
    visited[i][j] = True
    q = deque()
    q.append((i, j))

    while q:
        r, c = q.popleft()
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == board[i][j]:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                elif board[nr][nc] > board[i][j]: # 한번이라도 더 높은 곳 나오면 (i, j)는 산봉우리가 아닌 거임.
                    flag = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            flag = 1
            bfs(i, j)
            if flag:
                cnt += 1
print(cnt)

'''
8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 6 6 0 1 0
0 0 0 1 1 1 0
0 1 2 2 5 1 0
0 1 1 1 2 1 0
'''