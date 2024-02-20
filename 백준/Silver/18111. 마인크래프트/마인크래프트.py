# 아이디어 : 땅높이를 1로 맞출때 드는 시간, 2로 맞출때 ... 최대 높이로 맞출 때 걸리는 시간 중 최소로 출력
import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans_time = 256*N*M*3
ans_height = 0
for i in range(max(max(board))+1): # 최대 땅높이
    use_block = 0
    keep_block = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] > i:
                keep_block += board[x][y] - i
            else:
                use_block += i - board[x][y]
    if use_block > keep_block + B:
        continue

    count = use_block + keep_block*2

    if count <= ans_time:
        ans_time = count
        ans_height = i
print(ans_time, ans_height)
