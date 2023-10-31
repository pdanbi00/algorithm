from collections import deque


# R, G, B의 구역을 구하기
def bfs(sx, sy, color):
    q = deque()
    q.append((sx, sy))
    used[sx][sy] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not used[nx][ny] and data[nx][ny] == color:
                used[nx][ny] = 1
                q.append((nx, ny))


# R=G, B의 구역을 구하기
def bfs2(sx, sy, color):
    q = deque()
    q.append((sx, sy))
    used2[sx][sy] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not used2[nx][ny]:
                if color == 'R' or color == 'G':
                    if data[nx][ny] == 'R' or data[nx][ny] == 'G':
                        used2[nx][ny] = 1
                        q.append((nx, ny))
                elif color == 'B' and data[nx][ny] == 'B':
                    used2[nx][ny] = 1
                    q.append((nx, ny))


N = int(input())

data = [list(input()) for _ in range(N)]

ans1 = 0
ans2 = 0
used = [[0] * N for _ in range(N)]
used2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not used[i][j]:
            bfs(i, j, data[i][j])
            ans1 += 1
        if not used2[i][j]:
            bfs2(i, j, data[i][j])
            ans2 += 1

print(ans1, ans2)