import sys
input = sys.stdin.readline
N = int(input())
now_taps = list(map(int, input().split()))
right_taps = list(map(int, input().split()))

dif_taps = [0] * N
for i in range(N):
    dif_taps[i] = right_taps[i] - now_taps[i]

#  dp[i] : 1번부터 i번까지의 최소 인덴트 횟수수
dp = [0] * N
dp[0] = abs(dif_taps[0])

for i in range(1, N):
    # 현재 인덴트 차이와 다음 칸의 인덴트 차이의 부호가 같을 경우
    if dif_taps[i] * dif_taps[i-1] >= 0:
        dp[i] = dp[i-1] + max(0, abs(dif_taps[i]) - abs(dif_taps[i-1]))
    else:
        dp[i] = dp[i-1] + abs(dif_taps[i])
print(dp[N-1])