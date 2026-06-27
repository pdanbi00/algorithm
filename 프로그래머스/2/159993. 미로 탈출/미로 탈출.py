from collections import deque
def solution(maps):
    answer = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    N = len(maps)
    M = len(maps[0])
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                s_r, s_c = i, j
            elif maps[i][j] == 'E':
                e_r, e_c = i, j
            elif maps[i][j] == 'L':
                l_r, l_c = i, j
                
    # start -> 레버
    q = deque()
    q.append((s_r, s_c, 0))
    visited = [[False] * M for _ in range(N)]
    visited[s_r][s_c] = True
    possible = False
    while q:
        r, c, cnt = q.popleft()
        if r == l_r and c == l_c:
            answer += cnt
            possible = True
            break
            
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] != 'X' and not visited[nr][nc]:
                    q.append((nr, nc, cnt+1))
                    visited[nr][nc] = True
    
    if not possible:
        return -1
    # 레버 -> EXIT
    q = deque()
    q.append((l_r, l_c, 0))
    visited = [[False] * M for _ in range(N)]
    visited[l_r][l_c] = True
    possible = False
    while q:
        r, c, cnt = q.popleft()
        if r == e_r and c == e_c:
            answer += cnt
            possible = True
            break
            
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] != 'X' and not visited[nr][nc]:
                    q.append((nr, nc, cnt+1))
                    visited[nr][nc] = True
                    
    if not possible:
        return -1
    
    return answer