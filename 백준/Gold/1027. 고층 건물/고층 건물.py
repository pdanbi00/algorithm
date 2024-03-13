# i번째 빌딩 기준 왼쪽은 기준 빌딩에서 다음 빌딩 빼서 기울기 비교했을 때 그 앞까지 제일 작은 기울기보다 작으면 개수 추가
# i번째 빌딩 기준 오른쪽은 기준 빌딩에서 다음 빌딩 빼서 기울기 비교했을 때 그 전까지 제일 큰 기울기보다 크면 개수 추가
N = int(input())
buildings = list(map(int, input().split()))
dp = [0] * N
for i in range(N):
    view_max = 0
    left_max = float('inf')
    right_max = -float('inf')
    # 왼쪽 확인
    for j in range(i-1, -1, -1):
        degree = (buildings[i] - buildings[j]) / (i - j)
        if degree < left_max:
            view_max += 1
            left_max = degree
    # 오른쪽 확인
    for j in range(i +1, N):
        degree = (buildings[i] - buildings[j]) / (i - j)
        if degree > right_max:
            view_max += 1
            right_max = degree
    dp[i] = view_max
print(max(dp))