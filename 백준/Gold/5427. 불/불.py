from collections import deque
T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 0 : 방문 안함, 1 : 상근이, 2 : 불
def bfs(f_s, queue, visited): # 불의 bfs인지 상근이 bfs인지 구분
    while queue:
        r, c, time = queue.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < h and 0 <= nc < w:
                if board[nr][nc] == '.' or board[nr][nc] == '@':
                    if visited[nr][nc] > time + 1:
                        visited[nr][nc] = time + 1
                        queue.append((nr, nc, visited[nr][nc]))
            elif f_s == 's': # 상근이 이면 범위를 넘겼다는 말은 탈출했다는 의미
                print(time+1)
                return
    if f_s == 's':
        print("IMPOSSIBLE")

for _ in range(T):
    # 불이 먼저. 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없음.
    # 불이 오는 것과 동시에 다른 칸으로 이동 가능
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visited = [[1e9] * w for _ in range(h)]
    fire = deque()
    start = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire.append((i, j, 0)) # 행, 열, 시간
            if board[i][j] == '@':
                start.append((i, j, 0)) # 행, 열, 시간
    # 불과 관련된 bfs 먼저 처리하면서 불 확산 시간 기록해놓고
    # 상근이가 이동하면서 불 확산 시간 바탕으로 계속 이동
    bfs('f', fire, visited)
    bfs('s', start, visited)