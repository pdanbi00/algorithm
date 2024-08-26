from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    temp = []
    q.append((x, y))
    temp.append((x, y))
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(board[nr][nc] - board[r][c]) <= R:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    temp.append((nr, nc))
    return temp

answer = 0

while True:
    visited = [[False] * N for _ in range(N)]
    find = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                country = bfs(i, j)
                # 국경선이 모두 열렸다면 인구 이동 시작
                if len(country) > 1:
                    find = True
                    tmp = sum([board[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        board[x][y] = tmp

    if not find:
        print(answer)
        break
    answer += 1