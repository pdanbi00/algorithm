n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
answer = []
possible = True
for i in range(n):
    if visited[i]:
        continue
    visited[i] = True

    tmp = [i+1]
    for j in range(n):
        if i == j or board[i][j] == 1:
            continue
        if visited[j]:
            possible = False
            break
        visited[j] = True
        tmp.append(j+1)

    if len(tmp) < 2:
        possible = False
        break

    for k1 in tmp:
        for k2 in tmp:
            if board[k1-1][k2-1] == 1:
                possible = False
                break
        if not possible:
            break

    if not possible:
        break

    answer.append(tmp)

if possible:
    print(len(answer))
    for i in range(len(answer)):
        print(*answer[i])
else:
    print(0)