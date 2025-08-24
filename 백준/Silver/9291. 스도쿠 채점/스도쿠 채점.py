def check(arr):
    for i in range(9):
        visited_garo = [False] * 10
        visited_sero = [False] * 10

        for j in range(9):
            # 가로 확인
            if visited_garo[board[i][j]]:
                return False
            else:
                visited_garo[board[i][j]] = True

            # 세로 확인
            if visited_sero[board[j][i]]:
                return False
            else:
                visited_sero[board[j][i]] = True

            # 3 x 3 확인
            if i % 3 == 0 and j % 3 == 0:
                visited_three = [False] * 10
                for k in range(3):
                    for p in range(3):
                        if visited_three[board[i+k][j+p]]:
                            return False
                        else:
                            visited_three[board[i+k][j+p]] = True
    return True

T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    if tc != T:
        tmp = list(input())

    result = check(board)
    if result:
        print(f'Case {tc}: CORRECT')
    else:
        print(f'Case {tc}: INCORRECT')