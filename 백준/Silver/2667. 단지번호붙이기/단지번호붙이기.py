N  = int(input())
house = [list(map(int, input())) for _ in range(N)]
num = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    global count
    count += 1
    house[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if house[nx][ny] != 0:
                dfs(nx, ny)

count = 0
total = 0
for i in range(N):
    for j in range(N):
        if house[i][j] != 0:
            dfs(i, j)
            num.append(count)
            total += 1
            count = 0
num.sort()
print(total)
for i in num:
    print(i)