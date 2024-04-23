from collections import deque
def solution(maps):
    answer = 0
    n = len(maps) # 세로
    m = len(maps[0]) # 가로
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    find = False
    q = deque()
    q.append((0, 0, 1))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    cnt = 0
    while q:
        r, c, cnt = q.popleft()
        if r == n-1 and c == m-1:
            answer = cnt
            find = True
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == False and maps[nr][nc] == 1:
                    q.append((nr, nc, cnt+1))
                    visited[nr][nc] = True
    if not find:
        answer = -1
    return answer