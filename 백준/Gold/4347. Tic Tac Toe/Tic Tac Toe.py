N = int(input())
for tc in range(N):
    o_cnt = 0
    x_cnt = 0
    board = []
    for _ in range(3):
        arr = list(input())
        for j in range(3):
            if arr[j] == 'O':
                o_cnt += 1
            elif arr[j] == 'X':
                x_cnt += 1
        board.append(arr)
    if tc < N-1:
        tmp = input()

    # O가 이겼는지 확인하기
    o_win = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            o_win = True
        if board[0][i] == board[1][i] == board[2][i] == 'O':
            o_win = True
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        o_win = True
    if board[2][0] == board[1][1] == board[0][2] == 'O':
        o_win = True

    # X가 이겼는지 확인하기
    x_win = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'X':
            x_win = True
        if board[0][i] == board[1][i] == board[2][i] == 'X':
            x_win = True
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        x_win = True
    if board[2][0] == board[1][1] == board[0][2] == 'X':
        x_win = True


    answer = False
    if x_cnt == o_cnt + 1:
        if (x_win and not o_win) or (not x_win and not o_win):
            answer = True
    elif x_cnt == o_cnt:
        if (not x_win and o_win) or (not x_win and not o_win):
            answer = True
    elif x_cnt == 5 and o_cnt == 4 and not x_win and not o_win:
        answer = True

    if answer:
        print("yes")
    else:
        print("no")