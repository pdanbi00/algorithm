N, K = map(int, input().split())
bags = []
dp = [[0] * (K+1) for _ in range(N+1)] # 열은 0부터 K까지의 가방 무게를 의미. 행은 각 가방들을 의미
for i in range(N):
    W, V = map(int, input().split())
    bags.append((W, V))
for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= bags[i-1][0]: # 지금 무게가 물건 무게보다 크거나 같은 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bags[i-1][0]]+bags[i-1][1]) # i가 1부터 시작하니깐 bags[i-1]로 봐야됨.
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])