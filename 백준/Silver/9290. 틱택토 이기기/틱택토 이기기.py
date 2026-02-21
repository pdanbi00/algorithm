def check(target):
    # 가로 확인
    for i in range(3):
        if board[i][0] == target and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return True

    # 세로 확인
    for i in range(3):
        if board[0][i] == target and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return True

    # 대각1 확인
    if board[0][0] == target and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True

    # 대각2 확인
    if board[0][2] == target and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True

    return False

T = int(input())
for tc in range(T):
    board = [list(input()) for _ in range(3)]
    target = input()
    possible = False

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = target
                result = check(target)
                if result:
                    possible = True
                    break
                board[i][j] = '-'
        if possible:
            break

    print(f'Case {tc+1}: ')
    for i in range(3):
        print(''.join(board[i]))