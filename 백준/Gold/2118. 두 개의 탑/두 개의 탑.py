import sys
input = sys.stdin.readline
N = int(input())
dist = [int(input()) for _ in range(N)]

prefix_sum = [0] * (2 * N + 1)
for i in range(2 * N):
    prefix_sum[i+1] = prefix_sum[i] + dist[i % N]

ans = 0
total = sum(dist)
right = 1

for left in range(2 * N):
    # 시계 방향의 거리가 반시계방향의 거리보다 크면 거리 줄임
    while right < 2 * N + 1 and prefix_sum[right] - prefix_sum[left] <= total - (prefix_sum[right] - prefix_sum[left]):
        ans = max(ans, prefix_sum[right] - prefix_sum[left])
        right += 1
print(ans)