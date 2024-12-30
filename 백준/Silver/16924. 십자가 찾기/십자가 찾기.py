N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 각 *에서 이걸 중심으로 상하좌우 확인
# 상하좌우 다 * 이면 중심으로 체크
# 2칸씩, 3칸씩 더 확인해보기
# 상하좌우 다 확인 되면 체크하기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = []

def check(r, c):
    # r, c를 중심으로 상하좌우 확인
    length = 1
    while length <= (min(N, M) // 2):
        possible = True
        cnt = 0
        for k in range(4):
            nr = r + (dr[k] * length)
            nc = c + (dc[k] * length)
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] != '.':
                    cnt += 1
                else:
                    possible = False
                    break
        if possible and cnt == 4:
            if length == 1:
                if board[r][c] == '*':
                    board[r][c] = 0
                elif board[r][c] != '.':
                    board[r][c] += 1
            for k in range(4):
                nr = r + (dr[k] * length)
                nc = c + (dc[k] * length)
                if 0 <= nr < N and 0 <= nc < M:
                    if board[nr][nc] == '*':
                        board[nr][nc] = 0
                    elif board[nr][nc] != '.':
                        board[nr][nc] += 1
            answer.append((r+1, c+1, length))
            length += 1
        else:
            break

for i in range(N):
    for j in range(M):
        if board[i][j] != '.':
            check(i, j)
# print(board)
ans = True
for i in range(N):
    for j in range(M):
        if board[i][j] == '*':
            ans = False
            print(-1)
            exit()
print(len(answer))
for i in range(len(answer)):
    print(*answer[i])
