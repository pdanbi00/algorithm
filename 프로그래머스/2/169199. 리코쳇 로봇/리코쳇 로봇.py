from collections import deque
def solution(board):
    answer = -1
    N = len(board)
    M = len(board[0])
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                s_r = i
                s_c = j
            elif board[i][j] == "G":
                e_r = i
                e_c = j
                
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((s_r, s_c, 0))
    visited[s_r][s_c] = True
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q:
        r, c, cnt = q.popleft()
        if (r == e_r and c == e_c):
            answer = cnt
            break
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            while True:
                if 0 <= nr < N and 0 <= nc < M:
                    if board[nr][nc] != "D":
                        nr += dr[k]
                        nc += dc[k]
                        
                    else:
                        break
                else:
                    break
            nr -= dr[k]
            nc -= dc[k]
            if not visited[nr][nc]:
                q.append((nr, nc, cnt+1))
                visited[nr][nc] = True

    return answer