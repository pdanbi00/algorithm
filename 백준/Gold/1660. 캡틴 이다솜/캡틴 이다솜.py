N = int(input())

balls = [1] # 만들 수 있는 사면체

plus = 3 # 포탄이 늘어나는 개수
# 각 사면체를 만드는 데에 사용되는 대포알의 개수를 balls에 담기
for i in range(300001):
    if balls[i] >= N:
        break
    balls.append(balls[i] + plus)
    plus += (3+i)

dp = [300001] * (N+1)
# 대포알 개수에 따라 만들 수 있는 사면체 확인
for j in range(1, N+1):
    for k in balls:
        # 현재 대포알 개수로 사면체 만들 수 있으면
        if k == j:
            dp[j] = 1
            break
        # 대포알 개수로 사면체 만들 수 없다면
        if k > j:
            break

        # 현재 대포알의 개수로 만들 수 있는 사면체를 확인
        dp[j] = min(dp[j], 1 + dp[j-k])

print(dp[N])