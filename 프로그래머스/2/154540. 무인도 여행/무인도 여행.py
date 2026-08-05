from collections import deque
def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    visited = [[False] * M for _ in range(N)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                tmp = 0
                while q:
                    r, c = q.popleft()
                    tmp += int(maps[r][c])
                    
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < N and 0 <= nc < M:
                            if maps[nr][nc] != 'X' and not visited[nr][nc]:
                                q.append((nr, nc))
                                visited[nr][nc] = True
                answer.append(tmp)
    answer.sort()
    if not answer:
        answer = [-1]
    return answer