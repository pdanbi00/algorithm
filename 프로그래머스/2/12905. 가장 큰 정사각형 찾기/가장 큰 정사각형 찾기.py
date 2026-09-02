def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                if answer == 0:
                    answer = 1
                    
                if i-1 >= 0 and j-1 >= 0:
                    board[i][j] += min(board[i-1][j-1], board[i-1][j], board[i][j-1])
                    answer = max(answer, board[i][j])

    return answer * answer