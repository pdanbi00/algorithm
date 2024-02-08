# 이분탐색
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
s = 1
e = max(trees)
while s <= e:
    mid = (s+e) // 2
    total = 0
    for t in trees:
        if t >= mid:
            total += t-mid
    if total >= M:
        s = mid + 1
    else:
        e = mid - 1
print(e)