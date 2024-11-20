from itertools import combinations
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

arr = []
for i in range(N):
    for j in range(N):
        arr.append((i, j))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(i, j):
    tmp = board[i][j]
    visited[i][j] = 1
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            tmp += board[nr][nc]
            visited[nr][nc] = 1
        else:
            return ans
    return tmp

ans = 200*15

for combi in combinations(arr, 3):
    visited = [[0] * N for _ in range(N)]
    total = 0
    for com in combi:
        # print(com[0], com[1])
        total += bfs(com[0], com[1])
    ans = min(ans, total)
    # print('--------------')
print(ans)

