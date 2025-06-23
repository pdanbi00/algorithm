import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]

def check(R, C, arr):
    attached = False
    # 넣을 수 있는지 확인하기
    for i in range(N - R + 1):
        for j in range(M - C + 1):
            possible = True
            for r in range(R):
                for c in range(C):
                    if arr[r][c] == 1 and board[i+r][j+c] == 1:
                        possible = False
                        break
                if not possible:
                    break

            if possible:
                attached = True
                for r in range(R):
                    for c in range(C):
                        if block[r][c] == 1:
                            board[i+r][j+c] = 1
                break
        if attached:
            break
    return attached

def turn(R, C, block):
    new_block = [[0] * R for _ in range(C)]
    # 0행이 R-1 열로
    for i in range(R):
        for j in range(C):
            new_block[j][R-1-i] = block[i][j]
    return new_block

for i in range(K):
    R, C = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(R)]

    for _ in range(4):
        R = len(block)
        C = len(block[0])
        if check(R, C, block):
            # print('board check')
            # for i in range(N):
            #     print(board[i])
            break
        block = turn(R, C, block)
    #     for i in range(len(block)):
    #         print(block[i])
    # print('-------------')

cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cnt += 1

print(cnt)
