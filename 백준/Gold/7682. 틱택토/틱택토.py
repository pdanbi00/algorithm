# 한줄이 완성 됐는지 확인
def find_bingo(str):
    # 가로
    for i in range(3):
        if board[i][0] == str and board[i][0] == board[i][1] == board[i][2]:
            return True
    # 세로
    for i in range(3):
        if board[0][i] == str and board[0][i] == board[1][i] == board[2][i]:
            return True
    # 대각선
    if board[0][0] == str and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == str and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

while True:
    arr = input()
    if arr == 'end':
        break
    board = []
    O_cnt, X_cnt = 0, 0
    for i in range(3):
        a = []
        for j in range(3):
            a.append(arr[i*3 + j])
            if arr[i*3 + j] == 'X':
                X_cnt += 1
            elif arr[i*3 + j] == 'O':
                O_cnt += 1
        board.append(a)
    # print(board)
    # 가능한 경우
    # 1. 각 판에는 X는 5 개, O는 4개가 최대
    # 2. X부터 시작하기 때문에 X가 O보다 1개 더 많거나 같아야 됨
    #   - X개수랑 O개수 같으면 O가 이기는 경우여야 됨
    #   - X개수가 O개수보다 많으면 X가 이기는 경우로 끝나거나 가득찬 상태여야 됨.

    bingo_O, bingo_X = find_bingo('O'), find_bingo('X')
    # print(O_cnt, bingo_O, X_cnt, bingo_X)
    if bingo_X and not bingo_O and X_cnt == O_cnt + 1:
        print("valid")
        continue
    if bingo_O and not bingo_X and X_cnt == O_cnt:
        print("valid")
        continue
    if not bingo_O and bingo_X and O_cnt == 4 and X_cnt == 5:
        print("valid")
        continue
    if not bingo_O and not bingo_X and O_cnt == 4 and X_cnt == 5:
        print("valid")
        continue
    print("invalid")

