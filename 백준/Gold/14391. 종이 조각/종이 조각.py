# 0이면 가로 1이면 세로
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
ans = 0
for i in range(1<< (N*M)):
    total = 0
    # 가로 합
    for row in range(N):
        rowsum = 0
        for col in range(M):
            idx = row*M + col # 2차원 배열을 1차원 배열로 바꿨을때 인덱스
            if i & (1 << idx) == 0:
                rowsum = rowsum * 10 + board[row][col]
            else:
                total += rowsum
                rowsum = 0 # 한 줄에 가로인게 잘려서 여러개일수도 있으니깐
        total += rowsum

    # 세로 합
    for col in range(M):
        colsum = 0
        for row in range(N):
            idx = row*M + col
            if i & (1 << idx) != 0:
                colsum = colsum*10 + board[row][col]
            else:
                total += colsum
                colsum = 0
        total += colsum
    if ans < total:
        ans = total
print(ans)