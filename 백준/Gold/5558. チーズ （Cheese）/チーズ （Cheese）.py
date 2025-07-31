from collections import deque
import sys
input = sys.stdin.readline
H, W, N = map(int, input().rstrip().split())
board = []
cheeses = []
for i in range(H):
    arr = list(input().rstrip())
    for j in range(W):
        if arr[j] == 'S':
            cheeses.append((0, i, j))
        elif arr[j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            cheeses.append((int(arr[j]), i, j))
    board.append(arr)

cheeses.sort()
answer = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s_r, s_c, e_r, e_c):
    global answer
    q = deque()
    visited = [[-1] * W for _ in range(H)]
    q.append((s_r, s_c))
    visited[s_r][s_c] = 0

    while q:
        r, c = q.popleft()

        if r == e_r and c == e_c:
            answer += visited[r][c]
            break
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < H and 0 <= nc < W:
                if board[nr][nc] != 'X' and visited[nr][nc] == -1:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

for i in range(N):
    bfs(cheeses[i][1], cheeses[i][2], cheeses[i+1][1], cheeses[i+1][2])

print(answer)