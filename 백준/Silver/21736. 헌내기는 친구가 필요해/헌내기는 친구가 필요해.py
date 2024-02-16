# 이것은 누가봐도 bfs로 풀 수 있음
from collections import deque
N, M = map(int, input().split())
board = [input() for _ in range(N)]
checked= [[False] * M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0
find_ans = False
q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            find_ans = True
            q.append((i, j))
            checked[i][j] = True
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if board[nr][nc] != 'X' and not checked[nr][nc]:
                            q.append((nr, nc))
                            checked[nr][nc] = True
                            if board[nr][nc] == 'P':
                                ans += 1
            break
    if find_ans:
        break
if ans == 0:
    print('TT')
else:
    print(ans)


