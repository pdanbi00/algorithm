def dfs(r,c):
    stack = []
    stack.append((i, j))
    visited[i][j] = 1
    cnt = 0
    while stack:
        r, c = stack[-1]

        # 상하좌우
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and board[nr][nc] == 1:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                r = nr
                c = nc
                break
        else:
            stack.pop()
            cnt += 1
    return cnt



N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visited = [list([0] * N) for _ in range(N)]
total = 0
total_list = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            total += 1
            total_list.append(dfs(i,j))
# 오름차순으로 출력하라 했으니까 정렬
total_list.sort()
print(total)
for i in range(total):
    print(total_list[i])
