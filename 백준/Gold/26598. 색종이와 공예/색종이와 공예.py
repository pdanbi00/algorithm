from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

pretty = True

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 각 지점에서 bfs돌면서 같은거 있는 범위를 찾음. 그리고 그 범위 전체에 다른 문자 있는지 확인
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            q = deque()
            target = board[i][j]
            q.append((i, j))
            visited[i][j] = True
            min_r = N
            max_r = -1
            min_c = M
            max_c = -1

            while q:
                r, c = q.popleft()
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)

                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if board[nr][nc] == target and not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = True
            for r in range(min_r, max_r+1):
                for c in range(min_c, max_c+1):
                    if board[r][c] != target:
                        pretty = False
                        break
                if not pretty:
                    break
        if not pretty:
            break

    if not pretty:
        break

if pretty:
    print("dd")
else:
    print("BaboBabo")