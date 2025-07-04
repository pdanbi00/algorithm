import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
dr = [-1, 0, 1]
dc = [1, 1, 1]

def dfs(r, c):
    if c == C-1:
        return True

    result = False
    for k in range(3):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] != 'x' and not visited[nr][nc]:
                visited[nr][nc] = True
                result = dfs(nr, nc)
                if result:
                    return True
        else:
            continue
    return result

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
answer = 0
for i in range(R):
    if board[i][0] == '.':
        if dfs(i, 0):
            answer += 1

print(answer)