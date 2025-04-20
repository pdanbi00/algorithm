N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [(0, 1), (-1, 0), (-1, 0), (0, 1)]
dc = [(-1, 0), (0, -1), (0, 1), (1, 0)]

visited = [[False] * M for _ in range(N)]
answer = 0

def dfs(r, c, total):
    global answer
    # r, c 더이상 탐색할 수 없을 때 확인하기
    if c == M:
        r += 1
        c = 0

    if r == N:
        answer = max(answer, total)
        return

    if not visited[r][c]:
        for k in range(4):
            nr1 = r + dr[k][0]
            nc1 = c + dc[k][0]
            nr2 = r + dr[k][1]
            nc2 = c + dc[k][1]

            if 0 <= nr1 < N and 0 <= nr2 < N and 0 <= nc1 < M and 0 <= nc2 < M:
                if not visited[nr1][nc1] and not visited[nr2][nc2]:
                    visited[r][c] = True
                    visited[nr1][nc1] = True
                    visited[nr2][nc2] = True
                    tmp = board[r][c] * 2 + board[nr1][nc1] + board[nr2][nc2]
                    dfs(r, c+1, total+tmp) # 이번 칸을 선택하는 경우
                    visited[r][c] = False
                    visited[nr1][nc1] = False
                    visited[nr2][nc2] = False
    dfs(r, c+1, total)

dfs(0, 0, 0)
print(answer)
