from itertools import combinations
from collections import deque

board = [list(input()) for _ in range(5)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
position = []
for i in range(5):
    for j in range(5):
        position.append((i, j))

answer = 0

def checkDasom(arr):
    cnt = 0
    for r, c in arr:
        if board[r][c] == 'S':
            cnt += 1
    if cnt >= 4:
        return True
    else:
        return False

def checkAdjacent(arr):
    visited = [False] * 7
    q = deque()
    q.append(arr[0])
    visited[0] = True
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (nr, nc) in arr:
                n_idx = arr.index((nr, nc))
                if not visited[n_idx]:
                    q.append((nr, nc))
                    visited[n_idx] = True
    if False in visited:
        return False
    else:
        return True

for comb in combinations(position, 7):
    if checkDasom(comb):
        if checkAdjacent(comb):
            answer += 1

print(answer)