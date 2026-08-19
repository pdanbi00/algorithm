def solution(n, arr1, arr2):
    answer = []
    new_board = [['#'] * n for _ in range(n)]
    
    board1 = []
    for i in range(n):
        num = arr1[i]
        a = format(num, "b")
        board1.append(a.zfill(n))
    print(board1)
        
    board2 = []
    for i in range(n):
        num = arr2[i]
        a = format(num, "b")
        board2.append(a.zfill(n))
        
    for i in range(n):
        for j in range(n):
            if board1[i][j] == '0' and board2[i][j] == '0':
                new_board[i][j] = ' '
                
    for i in range(n):
        answer.append(''.join(new_board[i]))
    

    return answer