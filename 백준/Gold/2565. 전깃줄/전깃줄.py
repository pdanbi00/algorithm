N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
line.sort(key=lambda x : x[0])

# 교차된 줄이 없는 그룹 : A 전봇대 값을 오름차순으로 정렬한 상태에서 B 전봇대 값이 오름차순인 상태
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))