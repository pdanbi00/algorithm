from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
line = dict()
visited = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(i, j, color):
    q = deque()
    q.append((i, j))
    visited[i][j] = color
    line[color] = set()
    line[color].add((i, j))
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 1 and visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = color
                elif board[nr][nc] == 0:
                    line[color].add((r, c))

island = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and visited[i][j] == 0:
            island += 1
            bfs(i, j, island)
# 각 섬에서 나머지 섬들까지의 최소 거리 구하기
distance = [[1e9] * (island+1) for _ in range(island+1)]
edges = []

# i, j에서 한 방향으로 쭉 갔을 때 다른 섬 있는지 확인
def find(i, j, color):
    for k in range(4):
        r, c = i, j
        cnt = 0
        while True:
            r += dr[k]
            c += dc[k]
            cnt += 1
            if 0 <= r < N and 0 <= c < M:
                if visited[r][c] > 0 and visited[r][c] != color:
                    if cnt-1 >= 2:
                        distance[color][visited[r][c]] = min(distance[color][visited[r][c]], cnt - 1)
                        distance[visited[r][c]][color] = min(distance[visited[r][c]][color], cnt - 1)
                    break
                elif visited[r][c] == color:
                    break
            else:
                break

for k, v in line.items():
    for r, c in v:
        find(r, c, k)

edges = []
for i in range(1, island+1):
    for j in range(i+1, island+1):
        if distance[i][j] != 1e9:
            edges.append((distance[i][j], i, j))
edges.sort()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False
    if a < b:
        parent[b] = a

    else:
        parent[a] = b

    visited[a] = True
    visited[b] = True
    return True

ans = 0
parent = [i for i in range(island+1)]

visited = [False] * (island+1)
visited[0] = True
for cost, a, b in edges:
    if union(a, b):
        ans += cost

possible = True
for i in range(1, island+1):
    find(i)

for i in range(1, island):
    if parent[i] != parent[i+1]:
        possible = False
        break

if not possible:
    print(-1)
else:
    print(ans)
