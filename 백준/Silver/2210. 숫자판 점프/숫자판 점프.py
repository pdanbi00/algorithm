board = [list(map(str, input().split())) for _ in range(5)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = []

def dfs(r, c, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, number+board[nr][nc])

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(result))
