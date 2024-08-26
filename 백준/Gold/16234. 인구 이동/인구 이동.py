from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

# bfs돌면서 상하좌우 인구차이가 L명 이상 R명 이하인 곳들 모아놓기
# 한번에 숫자 바꾸기 전체 합 // 개수
# bfs에 채워지는게 없는 동안 진행

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    arr = []
    arr.append((x, y))

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and L <= abs(board[nr][nc] - board[r][c]) <= R:
                    q.append((nr, nc))
                    arr.append((nr, nc))
                    visited[nr][nc] = True
    change_idx.append(arr)

while True:
    find = False
    visited = [[False] * N for _ in range(N)]
    change_idx = [] # 국경선이 열리는 위치 넣을 배열
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                for k in range(4):
                    ni = i + dr[k]
                    nj = j + dc[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if not visited[ni][nj] and L <= abs(board[ni][nj] - board[i][j]) <= R:
                            bfs(i, j)
                            find = True
    for change in change_idx:
        tmp = 0
        for r, c in change:
            tmp += board[r][c]
        tmp //= len(change)
        for r, c in change:
            board[r][c] = tmp
    answer += 1
    if not find:
        print(answer-1)
        break
