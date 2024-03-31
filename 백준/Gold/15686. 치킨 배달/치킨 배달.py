# 전체 치킨 집 개수 중에 M개 고르기. -> 조합으로
# 골라서 큐에 다 집어넣고 bfs로 거리 다 구하기
# 거리 다 합한거랑 ans랑 비교해서 갱신
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 1e9

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))

def bfs(arr, board):
    ans = 0
    visited = [[0] * N for _ in range(N)]
    q = deque()
    for a in arr:
        q.append((a[0], a[1], a[0], a[1]))
        visited[a[0]][a[1]] = 1
    while q:
        r, c, p_r, p_c = q.popleft()
        if board[r][c] == 1:
            ans += abs(p_r - r) + abs(p_c - c)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 2 and visited[nr][nc] == 0:
                q.append((nr, nc, p_r, p_c))
                visited[nr][nc] = 1
    return ans

for com in combinations(chicken, M):
    arr = list(com)
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            board[i][j] = city[i][j]
            if (i, j) not in arr and city[i][j] == 2:
                board[i][j] = 0

    cnt = bfs(arr, board)
    if cnt < ans:
        ans = cnt
print(ans)
