from itertools import permutations

board = [list(input()) for _ in range(5)]
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
fill = [] # 채워야하는 위치
answer = []

for i in range(5):
    for j in range(9):
        if board[i][j] in alpha:
            alpha.remove(board[i][j])
        elif board[i][j] == 'x':
            fill.append((i, j))
# print(fill)
for perm in permutations(alpha, len(alpha)):
    possible = True
    for i in range(len(perm)):
        board[fill[i][0]][fill[i][1]] = perm[i]
    A = ord(board[1][1])-64 + ord(board[1][3])-64 + ord(board[1][5])-64 + ord(board[1][7])-64
    if A != 26:
        possible = False
        continue
    B = ord(board[3][1])-64 + ord(board[3][3])-64 + ord(board[3][5])-64 + ord(board[3][7])-64
    if B != 26:
        possible = False
        continue
    C = ord(board[0][4])-64 + ord(board[1][3])-64 + ord(board[2][2])-64 + ord(board[3][1])-64
    if C != 26:
        possible = False
        continue
    D = ord(board[0][4])-64 + ord(board[1][5])-64 + ord(board[2][6])-64 + ord(board[3][7])-64
    if D != 26:
        possible = False
        continue
    E = ord(board[4][4])-64 + ord(board[3][3])-64 + ord(board[2][2])-64 + ord(board[1][1])-64
    if E != 26:
        possible = False
        continue
    F = ord(board[4][4])-64 + ord(board[3][5])-64 + ord(board[2][6])-64 + ord(board[1][7])-64
    if F != 26:
        possible = False
        continue
    tmp = ''
    for i in range(5):
        tmp += ''.join(board[i])
    answer.append(tmp)
    break

arr = answer[0]
for i in range(len(arr)):
    if i % 9 != 8:
        print(arr[i], end='')
    else:
        print(arr[i])