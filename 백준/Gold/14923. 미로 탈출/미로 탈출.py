# BFS
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
s_r, s_c = map(int, input().split())
e_r, e_c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 3차원으로 만들자~~
# 깨고 진행한거랑 안 깨고 진행한거랑 렛츠 기릿
def bfs(s_r, s_c, e_r, e_c):
    q = deque()
    q.append((s_r, s_c, 0))
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    # visited[0][r][c]는 벽 안 깬 상태, visited[1][r][c]는 벽 깬 상태
    visited[0][s_r][s_c] = 1
    while q:
        r, c, b = q.popleft()
        if r == e_r and c == e_c:
            print(visited[b][r][c]-1)
            return
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                # 다음으로 이동할 곳이 벽이고, 벽을 아직 부수지 않은 경우
                if board[nr][nc] == 1 and b == 0:
                    q.append((nr, nc, 1))
                    visited[1][nr][nc] = visited[0][r][c] + 1
                # 다음으로 이동할 곳이 벽이 아니고, 아직 방문하지 않은 경우
                elif board[nr][nc] == 0 and visited[b][nr][nc] == 0:
                    q.append((nr, nc, b))
                    visited[b][nr][nc] = visited[b][r][c] + 1
    print(-1)
    return
bfs(s_r - 1, s_c - 1, e_r - 1, e_c - 1)

'''
5 6
1 1
5 6
0 1 1 1 0 0
0 1 1 0 0 0
0 1 0 0 1 0
0 1 0 0 1 0
0 0 0 1 1 0
'''