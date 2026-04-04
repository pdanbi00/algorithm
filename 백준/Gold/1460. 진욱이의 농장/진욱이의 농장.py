import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [[0] * N for _ in range(N)]

for _ in range(M):
    X, Y, L, F = map(int, input().split())

    for i in range(L):
        for j in range(L):
            board[Y+i][X+j] = F

# dp[i][j] : i행 j열이 오른쪽 아래 모서리일 경우 가장 넓은 크기
def search(t1, t2):
    tmp = 0
    dp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == t1 or board[i][j] == t2:
                dp[i][j] = 1

    for i in range(1, N):
        for j in range(1, N):
            if not dp[i][j]:
                continue
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            tmp = max(tmp, dp[i][j])
    return tmp

result = 0
# 씨앗은 최대 2종류이고 0번 씨앗은 안되니깐 1번 부터 7번 사이에서 2개 고른 경우로 다 살펴보기
for i in range(1, 8):
    for j in range(i+1, 8):
        result = max(result, search(i, j))

print(result**2)