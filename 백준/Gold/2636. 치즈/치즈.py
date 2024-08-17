# 역으로 생각해야됨.
# 공기에서 bfs를 돌고 치즈를 만나면 그 친구는 추가하기
from collections import deque

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans_time = 0
ans_cnt = 0

def bfs():
    q = deque()
    q.append((0, 0)) # 가장자리에는 치즈가 무조건 없다고 했으니
    visited[0][0] = True
    melt = deque() # 치즈인 부분 넣을 큐
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                visited[nr][nc] = True
                if board[nr][nc] == 0: # 공기이면 이어서 탐색하기 위해서 q에 넣기
                    q.append((nr, nc))
                elif board[nr][nc] == 1: # 치즈면 melt에 넣기
                    melt.append((nr, nc))

    for r, c in melt:
        board[r][c] = 0 # 공기랑 닿은 치즈 동시에 녹이기
    return len(melt) # 녹인 치즈 개수 반환

while True:
    visited = [[False] * C for _ in range(R)]
    cnt = bfs()
    if cnt != 0:
        ans_cnt = cnt
        ans_time += 1
    else:
        print(ans_time)
        print(ans_cnt)
        break
