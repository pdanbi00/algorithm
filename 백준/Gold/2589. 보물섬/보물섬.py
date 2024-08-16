from collections import deque
R, C = map(int, input().split())

board = [input() for _ in range(R)]
visited = [[-2] * C for _ in range(R)]

ans = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check_bfs(i, j):
    arr = [(i, j)]
    q = deque()
    q.append((i, j))
    visited[i][j] = -1
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] == 'L' and visited[nr][nc] == -2:
                    arr.append((nr, nc))
                    q.append((nr, nc))
                    visited[nr][nc] = -1
    return arr


def bfs(x, y):
    global ans
    queue = deque()
    queue.append((x, y))
    visit = [[-1] * C for _ in range(R)]
    visit[x][y] = 0
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] == 'L' and visit[nr][nc] == -1:
                    queue.append((nr, nc))
                    visit[nr][nc] = visit[r][c] + 1
                    ans = max(ans, visit[nr][nc])



# 1. 전체를 BFS를 돌아서 가장 칸 수가 많은 육지 찾아내기
for i in range(R):
    for j in range(C):
        if board[i][j] == 'L' and visited[i][j] == -2:
            # arr을 만들어서 연결된 육지들 넣기
            # 각 칸을 시작점으로 해서 가장 먼 곳까지의 거리 갱신하기
            array = check_bfs(i, j)
            for x, y in array:
                bfs(x, y)
print(ans)

'''
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
'''