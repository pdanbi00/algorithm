import sys
from collections import deque
input = sys.stdin.readline

# 서, 북, 동, 남
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    count = 1 # 방 크기

    while q:
        r, c = q.popleft()
        for k in range(4):
            if board[r][c] & (1<<k) == 0: # 벽이 없다는거임
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < M and 0 <= nc < N:
                    if visited[nr][nc] == False:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        count += 1
    return count


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
# 상하좌우로 살피는데 그 방향에 벽이 없어야 됨.
# 비트마스킹을 이용해서 성벽 유무 판단

# 방 개수
room_count = 0

# 가장 넒은 방의 크기
room_size = 0
visited = [[False]*N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            room_count += 1
            room_size = max(room_size, bfs(i, j))
print(room_count)
print(room_size)

# 하나의 벽 제거해서 얻을 수 있는 가장 넓은 방 크기 구하기
delete_wall_room_size = 0
for i in range(M):
    for j in range(N):
        for k in range(4):
            if board[i][j] & (1<<k) == (1<<k): # 벽이 있으면
                visited = [[False] * N for _ in range(M)]
                board[i][j] -= (1<<k) # 벽에 해당하는 수 만큼 빼서 벽을 없애줌
                delete_wall_room_size = max(delete_wall_room_size, bfs(i, j))
                board[i][j] += (1<<k) # 벽 복원

print(delete_wall_room_size)