N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# print(board)
minus_cnt = 0
zero_cnt = 0
plus_cnt = 0

def check(row, col, n):
    global minus_cnt, zero_cnt, plus_cnt
    curr = board[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if board[i][j] != curr:
                next_n = n // 3
                check(row, col, next_n) # 1
                check(row, col + next_n, next_n)  # 2
                check(row, col + (2 * next_n), next_n)  # 3

                check(row + next_n, col, next_n)  # 4
                check(row + next_n, col + next_n, next_n)  # 5
                check(row + next_n, col + (2 * next_n), next_n)  # 6

                check(row + (2 * next_n), col, next_n)  # 7
                check(row + (2 * next_n), col + next_n, next_n)  # 8
                check(row + (2 * next_n), col + (2 * next_n), next_n)  # 9
                return

    if curr == -1:
        minus_cnt += 1
    elif curr == 0:
        zero_cnt += 1
    elif curr == 1:
        plus_cnt += 1
    return

check(0, 0, N)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)