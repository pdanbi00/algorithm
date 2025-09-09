M, N  = map(int, input().split())
answer = [0] * 5
board = [list(input()) for _ in range(5 * M + 1)]
for i in range(1, 5 * M + 1, 5):
    for j in range(1, 5 * N + 1, 5):
        dot_cnt = 0
        star_cnt = 0
        for k in range(4):
            for p in range(4):
                if board[i+k][j+p] == '.':
                    dot_cnt += 1
                else:
                    star_cnt += 1
        if dot_cnt == 16:
            answer[0] += 1
        elif dot_cnt == 12:
            answer[1] += 1
        elif dot_cnt == 8:
            answer[2] += 1
        elif dot_cnt == 4:
            answer[3] += 1
        else:
            answer[4] += 1

print(*answer)