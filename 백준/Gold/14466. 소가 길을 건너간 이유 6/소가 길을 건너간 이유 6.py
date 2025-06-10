# 문제 해석 : 소가 다리 건너지 않고 갈 수 있는 길들을 다 체크
# 소가 안 겹치면 count 올리기
from collections import deque
N, K, R = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

road = [[[] for _ in range(N)] for _ in range(N)]

count = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    cow_visited[x][y] = True
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if not cow_visited[nr][nc]:
                    if (nr, nc) in road[r][c]:
                        continue
                    else:
                        q.append((nr, nc))
                        cow_visited[nr][nc] = True

for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1-1][c1-1].append((r2-1, c2-1))
    road[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))

cows = []
for i in range(K):
    r, c = map(int, input().split())
    cows.append((r-1, c-1))

for i in range(K):
    cow_visited = [[False] * N for _ in range(N)]
    r, c = cows[i][0], cows[i][1]
    bfs(r, c)

    for j in range(i+1, K):
        r2, c2 = cows[j][0], cows[j][1]
        if not cow_visited[r2][c2]:
            count += 1

print(count)