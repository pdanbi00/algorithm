T, W = map(int, input().split())
# dp[i][j] : i초동안 j번 움직였을 때 얻을 수 있는 최대 자두 수
# 1번 나무 밑에서 부터 시작하니깐 이동 횟수가 홀수면 2번 나무에 위치해있는거임

jadu = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W+1) for _ in range(T+1)]

for i in range(1, T+1):
    # 1번 나무에서 한번도 안 움직이는 경우
    if jadu[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    # 1번 이상 움직이는 경우
    for j in range(1, W+1):
        # i초에 2번 나무에서 자두 떨어지고, 지금 2번 나무에 있다면
        if jadu[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        # i초에 1번 나무에서 자두 떨어지고, 지금 1번 나무에 있다면
        elif jadu[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        # i초에 자두가 떨어지는 나무와 현재 나무 위치가 다르면
        else:
            # 움직여서 못 먹는 경우랑 안 움직여서 못 먹는 경우 둘 중 비교
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[T]))