# 이분 탐색
from bisect import bisect_left
import sys
input = sys.stdin.readline
N, H = map(int, input().split())
jong = []
suck = []
for i in range(N):
    height = int(input())
    if i % 2 == 0:
        suck.append(height)
    else:
        jong.append(height)
suck.sort()
jong.sort()

cnt = 0
min_height = N
for i in range(1, H+1):
    j = bisect_left(jong, H-i+1) # 종유석 중에 i 높이에 걸리지 않는 것들 개수
    s = bisect_left(suck, i) # 석순 중에 i 높이에 걸리지 않는 것들 개수
    total = N - (j+s)

    if min_height > total:
        min_height = total
        cnt = 1
    elif min_height == total:
        cnt += 1
print(min_height, cnt)
