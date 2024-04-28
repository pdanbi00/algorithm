# 이분탐색
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
simsa = [int(input()) for _ in range(N)]
l = min(simsa)
r = max(simsa) * M
answer = r

while l <= r:
    total = 0
    mid = (l+r) // 2

    for i in range(N):
        total += mid // simsa[i]

    if total >= M:
        r = mid - 1
        answer = min(answer, mid)

    else:
        l = mid + 1

print(answer)