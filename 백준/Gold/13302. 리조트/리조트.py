N, M = map(int, input().split())
# dp[i][j] : i -> 탐색하는 날짜, j -> 현재 갖고 있는 쿠폰의 수
# dp[i][j] : N번째 날에 M개의 쿠폰을 가지고 있는 경우
cant = []
if M != 0:
    cant = list(map(int, input().split()))

dp = [[1e9] * 106 for _ in range(106)]
dp[0][0] = 0

for i in range(N+1):
    for j in range(40): # 최대 쿠폰 개수 : 40개
        if dp[i][j] == 1e9:
            continue
        result = dp[i][j]

        # 리조트에 가지 못하는 경우
        if i + 1 in cant:
            dp[i+1][j] = min(result, dp[i+1][j])
        # 쿠폰이 3개 이상 있는 경우
        if j >= 3:
            dp[i+1][j-3] = min(result, dp[i+1][j-3])
        # 1일권 구매하는 경우
        dp[i+1][j] = min(result+10000, dp[i+1][j])
        # 3일권 구매하는 경우
        for k in range(1, 4):
            dp[i+k][j+1] = min(result + 25000, dp[i+k][j+1])
        # 5일권 구매하는 경우
        for k in range(1, 6):
            dp[i+k][j+2] = min(result + 37000, dp[i+k][j+2])
print(min(dp[N]))