#bfs
def bfs(s, e, cnt):
    visited = [[0] * M for _ in range(N)]
    queue = []
    queue.append((s, e, cnt))
    visited[s][e] = 1
    while queue:
        cr, cc, ccnt = queue.pop(0)
        if cr == N-1 and cc == M-1:
            return ccnt
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and board[nr][nc] == '1':
                queue.append((nr, nc, ccnt + 1))
                visited[nr][nc] = 1


N, M = map(int, input().split())
board = list(input() for _ in range(N))

result = bfs(0, 0, 1)
print(result)