import sys
input = sys.stdin.readline
M, N = map(int, input().split())
board = [[1] * M for _ in range(M)]
glow = [0] * (2 * M - 1) # 성장하는 정도

for _ in range(N):
    zero, one, two = list(map(int, input().split()))
    for i in range(zero, zero + one):
        glow[i] += 1

    for i in range(zero + one, 2 * M - 1):
        glow[i] += 2


idx = 0
# 제일 왼쪽 열부터 채우기
for i in range(M-1, 0, -1):
    board[i][0] += glow[idx]
    idx += 1

# 제일 위쪽 행 채우기
for j in range(M):
    board[0][j] += glow[idx]
    idx += 1

# 나머지 칸 채우기
# 항상 자기 자신 칸 위 칸이 최대 성장임
for i in range(1, M):
    for j in range(1, M):
        board[i][j] = board[i-1][j]

for i in range(M):
    print(*board[i])