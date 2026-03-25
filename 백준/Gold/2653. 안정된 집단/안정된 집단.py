n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
used = set()
answer = []
possible = True
for i in range(n):
    if tuple(board[i]) in used:
        continue
    used.add(tuple(board[i]))
    cnt = board[i].count(0)
    tmp = []
    for j in range(i, n):
        if board[j] == board[i]:
            tmp.append(j+1)

    if len(tmp) != cnt or len(tmp) < 2:
        possible = False
        break

    answer.append(tmp)

answer.sort()
if possible:
    print(len(answer))
    for i in range(len(answer)):
        print(*answer[i])
else:
    print(0)