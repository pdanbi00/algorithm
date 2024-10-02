# 최대한 빨리? bfs
from collections import deque

def solution(maps):
    answer = -1
    R = len(maps)
    C = len(maps[0])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    visited = [[0] * C for _ in range(R)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        r, c = q.popleft()
        if r == R-1 and c == C-1:
            answer = visited[r][c]
            break
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if visited[nr][nc] == 0 and maps[nr][nc] == 1:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
    return answer