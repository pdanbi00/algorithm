def solution(n):
    answer = []
    num = 1
    total = 0
    board = [[-1] * n for _ in range(n)]
    for i in range(1, n+1):
        total += i
    
    lap = 0
    while num <= total:
        # 아래로 내려가기
        for i in range(lap*2, n-lap):
            board[i][lap] = num
            num += 1
            if num > total:
                break
        if num > total:
                break
        # 마지막 행 다
        idx = lap+1
        while idx < n and board[n-(lap+1)][idx] == -1:
            board[n-(lap+1)][idx] = num
            num += 1
            idx += 1
            if num > total:
                break
        if num > total:
                break
        
        # 올라가기
        for i in range(n-(lap+2), lap*2, -1):
            board[i][i-lap] = num
            num += 1
            if num > total:
                break
        if num > total:
                break
        lap += 1
    
    for i in range(n):
        for j in range(n):
            if board[i][j] != -1:
                answer.append(board[i][j])
    
    return answer