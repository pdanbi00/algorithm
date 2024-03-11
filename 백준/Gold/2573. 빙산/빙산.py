# bfs로 1씩 줄인다.
# 그리고 나서 dfs로 전체 쪼개진거 확인
# 이거 계속하면 시간 터질거같은디
from collections import deque
import sys
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
possible = False
ans = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1 # 방문표시로 1로 처리하고 주변에 있는 얼음개수 만큼 +하니깐 메인에서 -1해줘야 됨.
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 0: # 주변 얼음 개수 체크
                    visited[r][c] += 1
                if visited[nr][nc] == 0 and graph[nr][nc] > 0: # 주변 빙하 체크
                    q.append((nr, nc))
                    visited[nr][nc] = 1

while True:
    # 빙하가 2개로 쪼개졌는지 확인
    bing_cnt = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and visited[i][j] == 0:
                bfs(i, j)
                bing_cnt += 1
    if bing_cnt == 0:
        print(0)
        break


    if bing_cnt >= 2:
        print(ans)
        break
    # 빙하가 2개이상으로 안 쪼개졌으면 1년 후로 계산해서 녹이기
    else:
        ans += 1
        for i in range(N):
            for j in range(M):
                if visited[i][j] > 0:
                    graph[i][j] -= (visited[i][j]-1)
                    if graph[i][j] < 0:
                        graph[i][j] = 0


