# dfs 돌면서 idx가 4이상일때 다시 원점으로 돌아오면 사이클이 있는 것
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

find = False
visited = [[False] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(s_r, s_c, i, j, idx):
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc] and board[nr][nc] == board[i][j]:
                visited[nr][nc] = True
                dfs(s_r, s_c, nr, nc, idx+1)
                visited[nr][nc] = False
            elif s_r == nr and s_c == nc and idx >= 4:
                print("Yes")
                exit()

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, i, j, 1)
        visited[i][j] = False


print("No")
