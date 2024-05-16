import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]

# 최단거리니깐 BFS. bfs큐에 벽 부순 개수 포함시켜서 하기
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)] # 방문횟수 표시
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
q = deque()
q.append((0, 0, K)) # r, c, 벽 부술 수 있는 횟수
visited[0][0][K] = 1
find = False
while q:
    r, c, cnt = q.popleft()
    if r == N-1 and c == M-1:
        print(visited[r][c][cnt])
        find = True
        break
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 1 and cnt > 0 and visited[nr][nc][cnt-1] == 0:
                visited[nr][nc][cnt-1] = visited[r][c][cnt] + 1
                q.append((nr, nc, cnt-1))

            elif board[nr][nc] == 0 and visited[nr][nc][cnt] == 0:
                visited[nr][nc][cnt] = visited[r][c][cnt] + 1
                q.append((nr, nc, cnt))
if not find:
    print(-1)
