def solution(board, h, w):
    answer = 0
    N = len(board)
    M = len(board[0])
    
    target = board[h][w]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for k in range(4):
        nr = h + dr[k]
        nc = w + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == target:
                answer += 1
    return answer