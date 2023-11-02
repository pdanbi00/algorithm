way = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y, visited, total):
    global answer
    if len(visited) == N + 1:
        answer += total
        return
    for idx in range(4):
        nx = x + way[idx][0]
        ny = y + way[idx][1]
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, visited, total * per[idx])
            visited.pop()


N, e, w, s, n = map(int, input().split())
per = [e, w, s, n]
answer = 0

dfs(0, 0, [(0, 0)], 1)
print(answer * (0.01 ** N))