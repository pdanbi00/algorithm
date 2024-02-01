# 이거는 회전 하는 수 제한이 10^9까지로 개많음.
# 그래서 배열돌리기 1처럼 푸는데 회전수를 미리 % 배열크기 해줘야 됨.
# 아이디어 : 회전하는 그룹을 각각 나눔.
#           나눈 그룹들을 일차원 배열로 만들어서 그 안에서 각각 회전 시키고
#           그 결과를 다시 넣어서 출력하기
N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
arrs = [] # 각 그룹들을 넣을 배열
arr_n = min(N, M) // 2 # 그룹의 개수
# 그룹 나누기
for k in range(arr_n):
    arr = []
    for j in range(k, M-k-1):
        arr.append(board[k][j])
    for i in range(k, N-k-1):
        arr.append(board[i][M-1-k])
    for j in range(M-k-1, k, -1):
        arr.append(board[N-1-k][j])
    for i in range(N-k-1, k, -1):
        arr.append(board[i][k])
    arrs.append(arr)
# 회전 시키기
for k in range(arr_n):
    group = arrs[k]
    l = len(group)
    index = R % l
    for j in range(k, M-k-1):
        board[k][j] = group[index]
        index = (index+1) % l
    for i in range(k, N-k-1):
        board[i][M-1-k] = group[index]
        index = (index+1) % l
    for j in range(M-1-k, k, -1):
        board[N-1-k][j] = group[index]
        index = (index+1) % l
    for i in range(N-1-k, k, -1):
        board[i][k] = group[index]
        index = (index+1) % l
for row in board:
    print(*row)