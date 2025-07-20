board = []
max_l = 0
for i in range(5):
    arr = list(input())
    max_l = max(max_l, len(arr))
    board.append(arr)

answer = ''
for j in range(max_l):
    for i in range(5):
        if len(board[i]) > j:
            answer += board[i][j]
print(answer)