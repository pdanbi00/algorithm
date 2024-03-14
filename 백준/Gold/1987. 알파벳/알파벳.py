from collections import deque
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
board = [input() for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 1
q = set()
q.add((0, 0, board[0][0]))
while q:
    r, c, line = q.pop()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] not in line:
                q.add((nr, nc, line+board[nr][nc]))
                ans = max(ans, len(line)+1)

print(ans)