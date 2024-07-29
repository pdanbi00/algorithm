
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[False] * N for _ in range(N)] # 각 방의 불 켜진지 상태 표시
board[0][0] = True

switch_dict = defaultdict(list) # 각 방에서 켤 수 있는 스위치 정보

for _ in range(M):
    x, y, a, b = map(int, input().split())
    switch_dict[(x-1, y-1)].append((a-1, b-1))
ans = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global ans
    q = deque()
    q.append((0, 0))
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True

    while q:
        r, c = q.popleft()
        # 해당 방에서 켤 수 있는 불부터 켜기
        for sr, sc in switch_dict[(r, c)]: # 현재 위치에서 불 켤 수 있는 곳
            if board[sr][sc] == False: # 아직 불 켜지지 않은 곳
                ans += 1
                board[sr][sc] = True
                if visited[sr][sc] == True:
                    q.append((sr, sc))
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == False:
                    visited[nr][nc] = True
                    if board[nr][nc] == True: # 불 켜져 있는 ㅏㅇ
                        q.append((nr, nc))


bfs()
print(ans)

