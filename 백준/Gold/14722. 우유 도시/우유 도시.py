# dp[k][i][j] : (i, j)에 도달할 때까지 가장 최근에 마신 우유가 k일 때 최대로 마신 우유의 개수
# dp[이전 우유 번호][이전 행][이전 열] == 0 -> 이전 칸의 우유를 마실 수 없는 경우
# 현재 칸에서 우유를 마실 수 없을 경우에는 이전 칸과 현재 칸 중 최댓값으로 저장
# 0번 우유(딸기 우유)는 앞에서 우유를 하나도 마시지 않은 경우 마실 수 있기 때문에 dp[0][0번 우유  r][0번 우유 c] = 1로 초기화
import sys
input = sys.stdin.readline

N = int(input())
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
board = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 0:
            dp[0][i][j] = 1
    board.append(arr)


dr = [0, -1]
dc = [-1, 0]

for r in range(N):
    for c in range(N):
        for k in range(2):
            pr = r + dr[k] # 이전 r
            pc = c + dc[k] # 이전 c
            if 0 <= pr < N and 0 <= pc < N:
                cur = board[r][c]
                pre = (cur + 2) % 3

                # 우유를 마실 수 없는 경우(가장 최근 마신 우유에 대한 데이터가 유지되어야하기 때문에 0, 1, 2 각각의 경우에만 해당)
                dp[0][r][c] = max(dp[0][r][c], dp[0][pr][pc])
                dp[1][r][c] = max(dp[1][r][c], dp[1][pr][pc])
                dp[2][r][c] = max(dp[2][r][c], dp[2][pr][pc])

                # 우유를 마실 수 있는 경우
                if dp[pre][pr][pc] > 0:
                    dp[cur][r][c] = max(dp[cur][r][c], dp[pre][pr][c] + 1)

print(max(dp[0][N-1][N-1], dp[1][N-1][N-1], dp[2][N-1][N-1]))