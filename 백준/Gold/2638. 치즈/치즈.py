# BFS로 돌면서 제일 테두리면 없애기
# 치즈를 탐색하는게 아니라 공기를 탐색

from collections import deque

# 공기 탐색
def air_bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                # 다음 진행이 공기면(큐에 추가, 방문 처리)
                if visited[nr][nc] == 0 and board[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                elif board[nr][nc] == 1:
                    visited[nr][nc] += 1

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
time = 0
while 1:
    visited = [[0] * M for _ in range(N)]
    air_bfs(0, 0)
    flag = False
    # 두 면 이상 공기에 닿으면 녹은거니깐 없애기
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                board[i][j] = 0
                flag = True

    if flag:
        time += 1
    else:
        break
print(time)