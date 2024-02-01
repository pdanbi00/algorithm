# 아이디어
# : 회전 하는 숫자들끼리를 한 그룹으로 묶어서
#   각 그룹 안에서 회전 각각 시키고 출력
#   그룹은 가로와 세로 중에 작은 값 // 2 한 만큼 나옴
N, M , R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
arrs = []
arr_n = min(N, M) // 2
for k in range(arr_n): # k번 그룹에 숫자 때려넣기
    arr = []
    for j in range(k, M-k-1): # 제일 윗 행들
        arr.append(board[k][j])
    for i in range(k, N-k-1): # 제일 오른쪽 열
        arr.append(board[i][M-1-k])
    for j in range(M-k-1, k, -1): # 제일 아래 행들
        arr.append(board[N-1-k][j])
    for i in range(N-k-1, k, -1): # 제일 왼쪽 열
        arr.append(board[i][k])
    arrs.append(arr)
# R번 만큼 회전시키기. 회전시키고 넣을 때 위에 꺼랑 순서 똑같아야 됨.
for k in range(arr_n):
    group = arrs[k]
    l = len(group)
    index = R % l # 크기가 10인걸 15번 회전 시키면 5번 회전 한거랑 같은 상태
    for j in range(k, M-k-1): # 제일 윗 행들
        board[k][j] = group[index]
        index = (index+1) % l
    for i in range(k, N-k-1): # 제일 오른쪽 열
        board[i][M-1-k] = group[index]
        index = (index+1) % l
    for j in range(M-k-1, k, -1): # 제일 아래 행들
        board[N-1-k][j] = group[index]
        index = (index+1) % l
    for i in range(N-k-1, k, -1): # 제일 왼쪽 열
        board[i][k] = group[index]
        index = (index+1) % l
# 출력
for row in board:
    print(*row)
