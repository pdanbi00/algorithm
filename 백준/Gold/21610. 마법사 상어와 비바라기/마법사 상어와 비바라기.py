# 시간 초과
# from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

dae_r = [-1, -1, 1, 1] # 단계 4에서 사용할 대각선들 방향
dae_c = [-1, 1, -1, 1] # 단계 4에서 사용할 대각선들 방향

clouds = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]


answer = 0

def rain(direction, distance):
    new_clouds = set()
    while clouds:
        # 구름 이동시키기
        r, c = clouds.pop()
        nr = (r + (dr[direction] * distance)) % N
        nc = (c + (dc[direction] * distance)) % N

        board[nr][nc] += 1
        new_clouds.add((nr, nc))

    # 단계 4
    for nr, nc in new_clouds:
        tmp = 0
        for k in [1, 3, 5, 7]:
            nnr = nr + dr[k]
            nnc = nc + dc[k]
            if 0 <= nnr < N and 0 <= nnc < N:
                if board[nnr][nnc] > 0:
                    tmp += 1
        board[nr][nc] += tmp

    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i, j) not in new_clouds:
                clouds.append((i, j))
                board[i][j] -= 2

for _ in range(M):
    direction, distance = map(int, input().split())
    rain(direction-1, distance % N)

answer = 0
for i in range(N):
    for j in range(N):
        answer += board[i][j]
print(answer)