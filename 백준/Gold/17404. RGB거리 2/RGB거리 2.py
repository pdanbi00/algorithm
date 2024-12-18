# 1번집은 2번, N번 집이랑 달라야함
# N번 집은 N-1, 1번 집이랑 달라야함
# i번 집은 i-1, i+1번 집이랑 달라야함
# -> 건물은 +1, -1과 같은 색으로 칠할 수 없음
#    1번째 건물이랑 N번째 건물은 같은 색으로 칠할 수 없음.
N = int(input())
# 빨강, 초록, 파랑 순서
board = [list(map(int, input().split())) for _ in range(N)]
ans = 1e9
# dp[i][j] : i번째 집을 j 색으로 칠했을때 최소 비용
dp = [[1001] * 3 for _ in range(N+1)]

# 첫번째 집에 칠할 색 k 정하기. 나머지 칸들은 칠할 수 없기 때문에 최댓값으로 설정
for k in range(3):
    for i in range(3):
        if k == i:
            dp[1][i] = board[0][i]
        else:
            dp[1][i] = 100001

    # 2번째 집부터 색칠하기
    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + board[i-1][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + board[i - 1][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + board[i - 1][2]

    # 정답 구하기
    for i in range(3):
        if i != k: # 첫번째 집 색이랑 마지막 집 색이랑 다를 경우
            ans = min(ans, dp[N][i])
print(ans)