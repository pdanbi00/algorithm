def solution(board, skill):
    # 누적합
    answer = 0
    tmp = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            tmp[r1][c1] -= degree
            tmp[r1][c2+1] += degree
            tmp[r2+1][c1] += degree
            tmp[r2+1][c2+1] -= degree
        else:
            tmp[r1][c1] += degree
            tmp[r1][c2+1] -= degree
            tmp[r2+1][c1] -= degree
            tmp[r2+1][c2+1] += degree
            
    # 누적합 구하기
    # 행 기준 누적합
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1] += tmp[i][j]
            
    # 열 기준 누적합
    for j in range(len(tmp[0])-1):
        for i in range(len(tmp)-1):
            tmp[i+1][j] += tmp[i][j]
            
    # 최종 계산
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer