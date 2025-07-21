N, M = map(int, input().split())
board = [[0] * M for _ in range(N+1)]
sum = [0] * (M)
for i in range(1, N+1):
    d, arr = input().split()
    for j in range(M):
        if arr[j] == '1':
            if d == 'L':
                value = -1
            else:
                value = 1

            sum[j] += value
            board[i][j] = value

answerTotal = 5000000
answerIdx = 0
for i in range(1, N+1):
    total = 0
    maxTotal = 0
    for j in range(M):
        total += sum[j] - board[i][j]
        maxTotal = max(maxTotal, abs(total))

    if answerTotal > maxTotal:
        answerTotal = maxTotal
        answerIdx = i

print(answerIdx)
print(answerTotal)