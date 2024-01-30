import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
q = deque()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 이거 하려면 1이 있는 곳에서 다 동시에 시작해야하기 때문에 다 큐에 넣어놓고 시작
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            # 익은 토마토 좌표 큐에 저장
            q.append((i, j))

while q:
    r, c = q.popleft()
    for k in range(4):
        nr, nc = r+dr[k], c+dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if tomato[nr][nc] == 0:
                q.append((nr, nc))
                tomato[nr][nc] = tomato[r][c] + 1



ans = 0
for row in tomato:
    for t in row:
        if t == 0:
            # 안익은 토마토 있으면 바로 -1 출력하고 중지
            print(-1)
            exit()
    ans = max(ans, max(row))
# 1부터 시작하는데 토마토는 하루 뒤부터 익으니깐 -1 해줘야됨
print(ans-1)